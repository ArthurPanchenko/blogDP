from dataclasses import fields
from pyexpat import model
from django import forms 
from .models import Post, Review


class CreatePostForm(forms.ModelForm):
    
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "What's happening?"
    }))
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['text', 'image']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text']