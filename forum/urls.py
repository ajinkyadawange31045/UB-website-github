from django.contrib import admin
from django.urls import path
app_name = 'forum'
from .views import (
    TopicCreateView,
    TopicListView,
    TopicDetailView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)
from . import views
from regi.views import ProfileView

urlpatterns = [
    path('forum/', TopicListView.as_view(), name='forum-index'),
    path('topic/add/', TopicCreateView.as_view(), name='topic-add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),

    path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    # path('profile/', v.profile, name='profile'),
    path('like/<int:pk>', views.like_view, name="like_post"),
    path('nested_comment/<int:id>', views.nested_comment, name="nested_comment"),
]
