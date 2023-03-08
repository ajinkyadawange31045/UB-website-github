from django.contrib import admin
from django.urls import path, include
from non_blogs.views import all_pages, youtube


urlpatterns = [
    path('all_posts/', all_pages, name="all_pages"),
    path('our_youtube_videos/',youtube)
    
]
