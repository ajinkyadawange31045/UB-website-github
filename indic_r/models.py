from django.db import models

class Competition(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
class Workshop(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='workshop_images/')

class Talk(models.Model):
    image = models.ImageField(upload_to='talk_images/')
    speaker_name = models.CharField(max_length=255)
    about_speaker = models.TextField()
    title_of_topic_of_speaker = models.CharField(max_length=255)
    about_talk_in_nutshell = models.TextField()

class Proshow(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True)
    short_content = models.CharField(max_length=255,null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='proshow_images/')

class SocialInitiative(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    short_content = models.CharField(max_length=255, null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='social_initiative_images/')
    
class Sponsor(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='sponsors/')

class EntityComment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    # created_date = models.DateTimeField(auto_now_add=True)
    
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, null=True, blank=True)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE, null=True, blank=True)
    proshow = models.ForeignKey(Proshow, on_delete=models.CASCADE, null=True, blank=True)
    social_initiative = models.ForeignKey(SocialInitiative, on_delete=models.CASCADE, null=True, blank=True)
