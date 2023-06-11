from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 100)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, blank=True, related_name="liked_images")
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title