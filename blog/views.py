from django.views.generic import ListView, DetailView, FormView, DeleteView, View, TemplateView
from django.views.generic.edit import FormMixin

from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import Post
from .forms import CreatePostForm, ReviewForm





class MainPageView(FormMixin, ListView):
    model = Post
    form_class = CreatePostForm
    context_object_name = 'posts'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.image = self.request.FILES['image']
            form.author = self.request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('home'))

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(text__icontains=q)
        return queryset


class PostDetailView(DetailView): 
    model = Post
    context_object_name = 'post'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'blog/post_delete.html'


def LikeView(request, pk):
    
    post = get_object_or_404(Post, pk=request.POST.get('post_id'))
    if post.likes.filter(pk=request.user.pk):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


class AddReviewView(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.post_id = pk
            form.author_id = request.user.pk
            form.save()
        return redirect(reverse('post-detail', kwargs={'pk': pk}))
