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

def forum_home(request):
    topics = Topic.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'topics':topics,
        'comments':comments,
        'posts':posts
    }
    return render(request,'forum_home.html',context)

def forum_post(request,pk):
    # topics = Topic.objects.all(pk=pk)
    topics = get_object_or_404(Topic,pk=pk)
    posts = Post.objects.all().filter(topic=topics)
    context = {
        'topics':topics,
        'posts':posts
    }
    return render(request,'forum_post.html',context)

def forum_comments(request,pk):
    posts = get_object_or_404(Post,pk=pk)
    comments = Comment.objects.all().filter(post=posts)
    context = {
        'comments':comments,
        'posts':posts
    }
    return render(request,'forum_comments.html',context)