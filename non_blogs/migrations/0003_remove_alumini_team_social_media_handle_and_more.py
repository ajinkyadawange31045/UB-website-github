# Generated by Django 4.1.2 on 2023-04-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_blogs', '0002_alumini_team_developer_team_media_team_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumini_team',
            name='Social_media_handle',
        ),
        migrations.RemoveField(
            model_name='alumini_team',
            name='handle_link',
        ),
        migrations.RemoveField(
            model_name='alumini_team',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='alumini_team',
            name='work',
        ),
        migrations.RemoveField(
            model_name='core_team',
            name='Social_media_handle',
        ),
        migrations.RemoveField(
            model_name='core_team',
            name='handle_link',
        ),
        migrations.RemoveField(
            model_name='core_team',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='developer_team',
            name='Social_media_handle',
        ),
        migrations.RemoveField(
            model_name='developer_team',
            name='handle_link',
        ),
        migrations.RemoveField(
            model_name='developer_team',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='media_team',
            name='Social_media_handle',
        ),
        migrations.RemoveField(
            model_name='media_team',
            name='handle_link',
        ),
        migrations.RemoveField(
            model_name='media_team',
            name='quote',
        ),
        migrations.AlterField(
            model_name='developer_team',
            name='work',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='media_team',
            name='work',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]