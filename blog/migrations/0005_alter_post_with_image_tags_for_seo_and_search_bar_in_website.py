# Generated by Django 4.1.2 on 2023-04-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_tags_for_seo_post_with_image_tags_for_seo_and_search_bar_in_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_with_image',
            name='tags_for_seo_and_search_bar_in_website',
            field=models.TextField(default='<django.db.models.fields.CharField>jo bhi'),
        ),
    ]
