from django import template
from blog.models import Post
from django.contrib.auth import get_user_model


register = template.Library()
User = get_user_model()


@register.simple_tag
def liked_by_user(post, user):
    if user in post.likes.all():
        return True
    return False
