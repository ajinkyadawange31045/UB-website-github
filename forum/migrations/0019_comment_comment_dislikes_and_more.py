# Generated by Django 4.1.2 on 2023-06-30 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0018_rename_likes_comment_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_comments_forum', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_dislikes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]