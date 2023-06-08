# Generated by Django 4.1.2 on 2023-06-05 03:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_post_with_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_with_image',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]