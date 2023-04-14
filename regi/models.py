import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Profile(models.Model):
    BRANCH_CHOICES = [
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('Chemical', 'Chemical'),
        ('Mining', 'Mining'),
        ('IT', 'IT'),
        ('Mech', 'Mech'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True,)
    phone_number = models.IntegerField(null=True, blank=True)
    # branch = models.CharField(choices=BRANCH_CHOICES, max_length=100, null=True, blank=True)
    # semester = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(default='../static/images/user_avtar.webp', upload_to='users/', null=True, blank=True)
    website = models.CharField(max_length=244 ,null=True, blank=True)
    github = models.CharField(max_length=244 ,null=True, blank=True)
    twitter = models.CharField(max_length=244 ,null=True, blank=True)
    instagram = models.CharField(max_length=244 ,null=True, blank=True)
    facebook = models.CharField(max_length=244 ,null=True, blank=True)
# final-ub-website-project\media\author\user_avtar.webp
    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=Profile)
def delete_previous_image(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_profile = Profile.objects.get(pk=instance.pk)
    except Profile.DoesNotExist:
        return False

    old_image = old_profile.profile_image
    new_image = instance.profile_image
    if old_image and old_image.name != new_image.name:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
