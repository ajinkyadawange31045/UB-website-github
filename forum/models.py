"""
Database models
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

 

class Topic(models.Model):
    """ Topics contain posts """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    
    def total_posts(self):
        return self.posts.count()

    def total_views(self):
        return sum(post.views for post in self.posts.all())

class Post(models.Model):
    """ Posts can be found under its topic. """

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True,related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, default='untitled')
    likes = models.ManyToManyField(User, related_name='forum_post')
    body = models.TextField()
    views = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post-detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """ Comments are replies to posts """

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.body

