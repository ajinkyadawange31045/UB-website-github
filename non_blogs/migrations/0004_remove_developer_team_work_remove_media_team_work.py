# Generated by Django 4.1.2 on 2023-04-04 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('non_blogs', '0003_remove_alumini_team_social_media_handle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer_team',
            name='work',
        ),
        migrations.RemoveField(
            model_name='media_team',
            name='work',
        ),
    ]