from django.contrib import admin
from django.urls import path, include
from non_blogs.views import all_pages, youtube, bookmark_blogs


urlpatterns = [
    path('all_posts/', all_pages, name="all_pages"),
    path('our_youtube_videos/',youtube),
    path('bookmarked_blogs/', bookmark_blogs, name="bookmarked_blogs")
]
