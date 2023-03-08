from django.urls import path
from . import views

urlpatterns = [
    path('indic-renaissance/', views.home, name='home'),
    path('competition/<int:pk>/', views.competition_detail, name='competition_detail'),
    path('workshop/<int:pk>/', views.workshop_detail, name='workshop_detail'),
    path('talk/<int:pk>/', views.talk_detail, name='talk_detail'),
    path('proshow/<int:pk>/', views.proshow_detail, name='proshow_detail'),
    path('social-initiative/<int:pk>/', views.social_initiative_detail, name='social_initiative_detail'),
]
