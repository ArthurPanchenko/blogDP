from pyexpat import model
from django.contrib import admin
from .models import Post, Review


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    
admin.site.register(Review)