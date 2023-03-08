from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
from .forms import SignUpForm, LoginForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from blog.models import Post_with_image,Author,Category,Comment
from non_blogs.models import Initiative, Team, Value, Future_events, Advertisement, Youtube_Video
from django import forms
from django.contrib.auth.models import Group
# from .forms import NewCommentForm, PostSearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# import math
# from itertools import chain
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# from math import random
from django.contrib.auth.decorators import login_required
# import time
# Create your views here.



def signup_redirect(request):
    # messages.error(request, "Something wrong here, it may be that you already have account!")
    # return redirect("homepage")
    return HttpResponse('Email already exist')


#logout________________________________________________________________________________________________
def user_logout(request):
    logout(request)
    # return HttpResponsePermanentRedirect('/')
    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))


#login________________________________________________________________________________________________
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request =request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    # return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))
                    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))
                    # return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = LoginForm()
        return render(request,'registration/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')


#signup________________________________________________________________________________________________
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Signed Up successfully')
                user = form.save()
                return HttpResponseRedirect('/login/')
                # group = Group.objects.get(name ='Author')
                # user.groups.add(group)
        else:
            form = SignUpForm()
        return render(request,'registration/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

# user profile________________________________________________________________________________________________
def user_profile(request):\
    
    if request.user.is_authenticated:
        if request.method == "POST":
            fm  = EditUserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                messages.success(request,'Profile has been updated')
                fm.save()
        else:
            fm = EditUserProfileForm(instance= request.user)
        return render(request,'registration/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# change password________________________________________________________________________________________________
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'registration/change_pass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

