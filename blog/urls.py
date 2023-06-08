from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home, post,category,post_search,about, add_likes, add_bookmark


urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('about/',about),
    path('category/<slug:url>',category),
    path('search/', post_search, name="search"),
    path('likes/<int:ids>', add_likes, name="likes"),
    path('bookmark/<int:ids>', add_bookmark, name="bookmark")
]
