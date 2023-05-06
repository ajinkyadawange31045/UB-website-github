from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from blog.models import Post_with_image,Author,Category
from non_blogs.models import Initiative,  Value, Advertisement, Youtube_Video
from django import forms



#  page which displays video regarding bharath
def youtube(request):
    yt = Youtube_Video.objects.all()
    first_4_categories = Category.objects.all()[0:4]
    remaining_categories = Category.objects.all()[::-1]
    data = {'yt':yt,'cat_4': first_4_categories,'cat_r':remaining_categories,}
    return render(request,'non_blog/youtube.html',data)


# all pages________________________________________________________________________________________________
def all_pages(request):
    post = Post_with_image.objects.all().order_by('-blog_views')
    first_4_categories = Category.objects.all()[0:4]
    remaining_categories = Category.objects.all()[::-1]
    data = {'post':post,'cat_4': first_4_categories,'cat_r':remaining_categories,}
    return render(request,'non_blog/blog_page.html',data)


