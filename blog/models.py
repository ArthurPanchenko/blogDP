from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """Model for post"""

    text = models.TextField()
    image = models.ImageField(upload_to='post_pics', null=True)
    published_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    class Meta:
        ordering = ['-published_time']

    def __str__(self):
        return self.text[:20]

    def get_likes_count(self):
        return self.likes.count()

    def get_reviews(self):
        return self.review_set.filter(parent__isnull=True)


class Review(models.Model):

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    published_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_time']

    def __str__(self):
        return f'{self.author} {self.post}'
