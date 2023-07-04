from django.shortcuts import render, reverse,HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.db.models import Sum
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
from crispy_forms.helper import FormHelper

from forum.models import Topic, Post, Comment
# from forum.forms import CreateCommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from forum.models import Post
# from .forms import MyForm

# def my_view(request):
#     form = MyForm()
#     context = {'form': form}
#     return render(request, 'my_template.html', context)

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from forum import views
# @login_required
# def forum_home(request):
#     return redirect('forum:forum-index')

# @login_required
# def forum_post(request, pk):
#     return redirect('forum:topic-detail')

# @login_required
# def forum_comments(request, pk):
#     return redirect('forum:post-detail')


def forum_home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('forum:forum-index'))
    topics = Topic.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'topics':topics,
        'comments':comments,
        'posts':posts
    }
    return render(request,'forum_home.html',context)
from django.shortcuts import redirect

def forum_post(request, pk):
    if request.user.is_authenticated:
        # If the user is logged in, redirect to the corresponding view in the 'forum' app
        return redirect('forum:topic-detail', pk=pk)
    
    # If the user is not logged in, render the 'no_login_forum' view as before
    topics = get_object_or_404(Topic, pk=pk)
    posts = Post.objects.filter(topic=topics)
    context = {
        'topics': topics,
        'posts': posts
    }
    return render(request, 'forum_post.html', context)


def forum_comments(request,pk):
    if request.user.is_authenticated:
         return redirect('forum:post-detail', pk=pk)
    posts = get_object_or_404(Post,pk=pk)
    comments = Comment.objects.all().filter(post=posts)
    # viewed_posts =[]
    posts.views += 1
    posts.save()
    # viewed_posts.append(post.id)
    context = {
        'comments':comments,
        'posts':posts
    }
    return render(request,'forum_comments.html',context)