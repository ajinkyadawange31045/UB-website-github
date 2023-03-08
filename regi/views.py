from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
# from .forms import SignUpForm, LoginForm,EditUserProfileForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
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
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, User
from django.views.generic import TemplateView, CreateView

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.dispatch import receiver

#logout________________________________________________________________________________________________
def user_logout(request):
    logout(request)
    # return HttpResponsePermanentRedirect('/')
    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))


#login________________________________________________________________________________________________
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request = request,data=request.POST)
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
        return render(request,'regi/login.html',{'form':form})
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
        return render(request,'regi/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

# def profile_view(request):
    
    
# user profile________________________________________________________________________________________________
# def user_profile(request):\
    
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             fm  = EditUserProfileForm(request.POST, instance = request.user)
#             if fm.is_valid():
#                 messages.success(request,'Profile has been updated')
#                 fm.save()
#         else:
#             fm = EditUserProfileForm(instance= request.user)
#         return render(request,'regi/profile.html',{'name':request.user,'form':fm})
#     else:
#         return HttpResponseRedirect('/login/')

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
        return render(request,'regi/change_pass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')




from django.urls import reverse
from forum.models import Post, Comment

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'regi/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user's forum posts and count them
        user_forum_posts = Post.objects.filter(author=self.request.user)
        context['num_forum_posts'] = user_forum_posts.count()

        # Get the users comments on forum posts and count them
        user_comments = Comment.objects.filter(author=self.request.user)
        context['num_comments'] = user_comments.count()

        # Get the user's posts and add links to them
        user_posts = Post.objects.filter(author=self.request.user)
        context['num_posts'] = user_posts.count()
        context['user_posts'] = []
        for post in user_posts:
            post_url = reverse('post-detail', kwargs={'pk': post.pk})
            context['user_posts'].append({'post': post, 'post_url': post_url})

        return context




class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'regi/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# from django.shortcuts import render
# from django.contrib.auth.models import User
# from .models import Profile

# def public_profile(request, username):
#     user = User.objects.get(username=username)
#     profile = Profile.objects.get(user=user)
#     context = {'profile': profile}
#     return render(request, 'regi/public_profile.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count

from .models import Profile
from forum.models import Post, Comment
@login_required
def public_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    # Get the user's forum posts and count them
    user_forum_posts_count = Post.objects.filter(author=user).count()

    # Get the users comments on forum posts and count them
    user_comments_count = Comment.objects.filter(author=user).count()

    # Get the user's posts and add links to them
    user_posts = Post.objects.filter(author=user)
    user_posts_count = user_posts.count()
    user_posts_with_urls = []
    for post in user_posts:
        post_url = reverse('post-detail', kwargs={'pk': post.pk})
        user_posts_with_urls.append({'post': post, 'post_url': post_url})

    context = {
        'profile': profile,
        'num_forum_posts': user_forum_posts_count,
        'num_comments': user_comments_count,
        'num_posts': user_posts_count,
        'user_posts': user_posts_with_urls
    }
    return render(request, 'regi/public_profile.html', context)
