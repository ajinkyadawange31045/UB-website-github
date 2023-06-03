from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

# team
class Alumini_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # work = models.CharField(max_length=20)
    # quote = models.CharField(max_length=40,blank=True,default="no use, don't write anything")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name

class Core_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    # quote = models.CharField(max_length=40,blank=True,default="no use, don't write anything")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name

class Third_year_core_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    work = models.CharField(max_length=200,blank=True, null=True)
    # quote = models.CharField(max_length=40,blank=True,default="no use, don't write anything")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name

class Developer_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # work = models.CharField(max_length=20,blank=True, null=True)
    # quote = models.CharField(max_length=40,blank=True,default="no use, don't write anything")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name

class Web_content_management_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # work = models.CharField(max_length=20,blank=True, null=True)
    # quote = models.CharField(max_length=40,blank=True,default="no use, don't write anything")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/')
    def __str__(self):
        return self.name


class Initiative(models.Model):
    initiative_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    title1_like_what_we_do = models.CharField(max_length=45, blank=True)
    content1 = models.CharField(max_length=200, blank=True)
    title2_like_how_we_do = models.CharField(max_length=45, blank=True)
    content2 = models.CharField(max_length=200, blank=True)
    title_like_what_we_achieve = models.CharField(max_length=45, blank=True)
    content3 = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='initiatives/')
    date_of_initiative = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


# Values of club
class Value(models.Model):
    value_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    quote = models.TextField(max_length=1000)
    thumbnail  = models.ImageField(upload_to='value/')
    def __str__(self):
        return self.name

# Advertisement
class Advertisement(models.Model):
    add_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,blank=True)
    content = models.TextField(max_length=1000,blank=True)
    image  = models.ImageField(upload_to='add/',blank=True)
    # url = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)
    
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'


# for future events
class Past_events(models.Model):
    title = models.CharField(max_length=100)
    options = (
        ('Jan','1'),
        ('Feb','2'),
        ('Mar','3'),
        ('Apr','4'),
        ('May','5'),
        ('June','6'),
        ('July','7'),
        ('Aug','8'),
        ('Sept','9'),
        ('Oct','10'),
        ('Nov','11'),
        ('Dec','12'),
    )
    date_of_event = models.IntegerField()
    month_of_event = models.CharField(max_length=10, choices=options)
    any_hashtag = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    

from embed_video.fields import EmbedVideoField
# Create your models here.
class Youtube_Video(models.Model):
    title=models.CharField(max_length=50)
    # date=models.DateTimeField(auto_now_add=False)
    video=EmbedVideoField()
    def __str__(self):
        return self.title