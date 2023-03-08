from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from auths.views import user_signup, user_login, user_logout,user_change_pass,user_profile
from . import views

urlpatterns = [
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('profile/', user_profile, name="profile"),
    path('user_change_pass/', user_change_pass, name="change_pass"),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
]
