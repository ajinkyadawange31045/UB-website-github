# Generated by Django 4.1.2 on 2023-03-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('short_content', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='proshow_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialInitiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('short_content', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='social_initiative_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='sponsors/')),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='talk_images/')),
                ('speaker_name', models.CharField(max_length=255)),
                ('about_speaker', models.TextField()),
                ('title_of_topic_of_speaker', models.CharField(max_length=255)),
                ('about_talk_in_nutshell', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='workshop_images/')),
            ],
        ),
        migrations.CreateModel(
            name='EntityComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indic_r.competition')),
                ('proshow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indic_r.proshow')),
                ('social_initiative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indic_r.socialinitiative')),
                ('talk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indic_r.talk')),
                ('workshop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indic_r.workshop')),
            ],
        ),
    ]
