from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 100)
    tags = TaggableManager()

    def __str__(self):
        return self.title