from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post
from .forms import CustomUserChangeForm

User = get_user_model()


class ProfileDetailView(FormMixin, DetailView):
    model = User
    template_name = 'account/profile_detail.html'
    context_object_name = 'user'
    form_class = CustomUserChangeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author__pk=self.kwargs.get('pk'))
        context['posts_count'] = len(context['posts'])
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.first_name = self.request.POST.get('first_name')
            form.last_name = self.request.POST.get('last_name')
            form.image = self.request.FILES.get('image')
            form.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'pk': self.kwargs['pk']}))