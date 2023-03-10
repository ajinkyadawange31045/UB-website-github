# Generated by Django 4.1.2 on 2022-12-25 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='author/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('url', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post_with_image',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('blog_views', models.IntegerField(default=0, editable=False)),
                ('main_long_title', models.CharField(max_length=250)),
                ('excerpt', models.TextField(max_length=1000)),
                ('thumbnail', models.ImageField(upload_to='post_thumbnail/')),
                ('thumbnail_caption', models.CharField(default='Image related to blog', max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_before_image', models.TextField(blank=True)),
                ('image_for_post', models.ImageField(blank=True, upload_to='image_for_post/')),
                ('caption_for_image', models.CharField(blank=True, max_length=100)),
                ('content_after_image', models.TextField(blank=True)),
                ('quote_related_to_post', models.TextField(blank=True)),
                ('author_of_quote', models.CharField(blank=True, max_length=50)),
                ('tags_for_seo', models.TextField(default='Utkrishta Bharath,Utkrishta Bharath NITK, Utkrishta Bharath nitk, India, Glories of India, ancient india, making india Utkrishta, facebook-Utkrishta Bharath, twitter-Utkrishta Bharath, linkedIn-Utkrishta Bharath, Bharath Darshan,')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post_with_image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
