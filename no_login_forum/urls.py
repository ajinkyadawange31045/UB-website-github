from django.contrib import admin
from django.urls import path
app_name = 'no_login_forum'
from .views import (
    # TopicCreateView,
    forum_home,
    forum_comments,
    forum_post
    
)
from . import views
# from regi.views import ProfileView

urlpatterns = [
    path('indirect-forum/', forum_home, name='forum-index-indirect'),
    path('indirect-topic/<int:pk>/', forum_post, name='topic-detail-indirect'),

    # path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('indirect-post/<int:pk>/', forum_comments, name='post-detail-indirect'),
    # path('indirect-like/<int:pk>', views.like_view, name="like_post-indirect")
]


# from django.contrib import admin
# from django.urls import path
# from django.views.generic.base import RedirectView

# app_name = 'no_login_forum'

# urlpatterns = [
#     path('indirect-forum/', RedirectView.as_view(url='/forum/'), name='forum-index-indirect'),
#     path('indirect-topic/<int:pk>/', RedirectView.as_view(pattern_name='forum:topic-detail', permanent=False), name='topic-detail-indirect'),
#     path('indirect-post/<int:pk>/', RedirectView.as_view(pattern_name='forum:post-detail', permanent=False), name='post-detail-indirect'),
# ]
