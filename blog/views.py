from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from blog.models import Post_with_image,Author,Category,Comment
from non_blogs.models import Initiative, Core_Team, Value, Past_events, Advertisement, Youtube_Video
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
from non_blogs.forms import ContactForm
from blog.forms import PostSearchForm,NewCommentForm
from django.urls import reverse
# import time
# from community.models import Question
# from community.views import 

@login_required
def add_likes(request, ids) :
    if request.user.is_authenticated :
        if request.method == "POST" :
            user = request.user
            get_post = Post_with_image.objects.get(post_id = ids)
            if user in get_post.likes.all() :
                get_post.likes.remove(user)
            else :
                get_post.likes.add(user)
            return HttpResponseRedirect(reverse(post, args=(get_post.url, )))
        
@login_required
def add_bookmark(request, ids) :
    if request.user.is_authenticated :
        if request.method == "POST" :
            user = request.user
            get_post = Post_with_image.objects.get(post_id = ids)
            if user in get_post.bookmark.all() :
                get_post.bookmark.remove(user)
            else :
                get_post.bookmark.add(user)
            return HttpResponseRedirect(reverse(post, args=(get_post.url, )))



# sidebar recomendation things algo________________________________________________________________
def sidebar():
    post1 = Post_with_image.objects.all()
    try:
        latest = post1[0:5]
    except latest1.DoesNotExist:
        latest = None
    try:
        latest1 = post1[5:10]
    except latest1.DoesNotExist:
        latest1 = None
    try:
        latest2 = post1[10:15]
    except latest2.DoesNotExist:
        latest2 = None
    try:
        latest3 = post1[15:20]
    except latest2.DoesNotExist:
        latest3 = None


    try:
        main = Category.objects.annotate()[0]
        post_main = Post_with_image.objects.filter(category=main)[0:5]
    except:
        main = None
        post_main = None
    
    try:
        first = Category.objects.annotate()[1]
        post_first = Post_with_image.objects.filter(category=first)[0:5]
    except:
        first = None
        post_first = None
    
    try:
        second = Category.objects.annotate()[2]
        post_second = Post_with_image.objects.filter(category=second)[0:5]
    except:
        second = None
        post_second = None
    
    try:
        third = Category.objects.annotate()[3]
        post_third = Post_with_image.objects.filter(category=third)[0:5]
    except:
        third = None
        post_third = None
    
    try:       
        forth = Category.objects.annotate()[4]
        post_forth = Post_with_image.objects.filter(category=forth)[0:5]
    except:
        forth = None
        post_forth = None
    
    try:       
        fifth = Category.objects.annotate()[5]
        post_fifth = Post_with_image.objects.filter(category=fifth)[0:5]
    except:
        fifth = None
        post_fifth = None
    
    try:       
        sixth = Category.objects.annotate()[6]
        post_sixth = Post_with_image.objects.filter(category=sixth)[0:5]
    except:
        sixth = None
        post_sixth = None
    recomendation_things = {'sidebar_latest':latest,'latest':latest,'latest1':latest1,'latest2':latest2,'latest3':latest3,'post_main':post_main,'post_first':post_first,'post_second':post_second,'post_third':post_third,'post_forth':post_forth,'post_fifth':post_fifth,'post_sixth':post_sixth,}
    return recomendation_things


# Home________________________________________________________________________________________________
def home(request):
    all_categories = Category.objects.all()
    first_4_categories = Category.objects.all()[0:4]
    remaining_categoreis = Category.objects.all()[::-1]
    # initiatives
    initiatives = Initiative.objects.all()
    # future values
    future = Past_events.objects.all()
    try:
        adv1 = Advertisement.objects.all()[0]
    except:
        adv1 = None
    try:
        adv2 = Advertisement.objects.all()[1::]
    except:
        adv2 = None
        
    # sidebar
    x_one = sidebar() 
    # sidebar ends

    posts = Post_with_image.objects.all()[:11]
    # print(posts)
    try:
        team_core_members = Core_Team.objects.all()
    except:
        tean_core_members = None
    
    
    
    values = Value.objects.all()
    
    # contact form
    user_comment = None
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            user_comment = contact_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/')
    else:
        contact_form = ContactForm()

    post1 = Post_with_image.objects.all()
    latest = post1[0:4] 
    
    
    # post with most views
    try:
        aj = Post_with_image.objects.all().order_by('-blog_views')[0:20]
        # aj.blog_views_top()
    except:
        aj = None

    data = {'all_categories':all_categories,'posts': posts,'cat_4': first_4_categories,'cat_r':remaining_categoreis,'team_core_members':team_core_members,'values':values,'contact_form':contact_form,'user_comment':user_comment,"initiatives":initiatives,'future':future,'adv1':adv1,'adv2':adv2,'aj':aj,'user': request.user,}
    
    # merging above dictionaries
    data_final = {**x_one,**data}
    return render(request, "blog/home.html", data_final)



# blog post________________________________________________________________________________________________
def post(request, url):
    remaining_categoreis = Category.objects.all()[::-1]
    post = Post_with_image.objects.filter(url=url).first()
    cats = Category.objects.all()
    datetime = Post_with_image.objects.all()
    future = Past_events.objects.all()
    try:
        adv1 = Advertisement.objects.all()[0]
    except:
        adv1 = None
    try:
        adv2 = Advertisement.objects.all()[1::]
    except:
        adv2 = None
   
#    comment section
    post_comment =Post_with_image.objects.filter(url=url).first()
    comments = post.comments.filter(status=True)
    allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(allcomments, 20)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    # view count on each blog
    blog_object=Post_with_image.objects.get(url=url)
    blog_object.blog_views=blog_object.blog_views+1
    value = str(blog_object.blog_views)
    if value.isdigit():
        value_int = int(value)
        if value_int > 1000000:
            value = "%.1f%s" % (value_int/1000000.00, 'M')
        else:
            if value_int > 1000:
                value = "%.1f%s" % (value_int/1000.0, 'k')
    # print(value)
    blog_object.save()
    # time.sleep(2)

    # comment section 
    user_contact = None
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_contact = comment_form.save(commit=False)
            user_contact.post = post
            user_contact.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = NewCommentForm()
    

    # sidebar
    # x_one = sidebar()
    post_ard = Post_with_image.objects.all()
    try:
        latest = post_ard
    except latest.DoesNotExist:
        latest = None

    blog = Post_with_image.objects.get(url=url)
    like_count = blog.likes.count()
    liked = blog.likes.filter(id=request.user.id).exists()
    is_bookmarked = blog.bookmark.filter(id=request.user.id).exists()


    data = {'post':post,'cats':cats,'datetime':datetime,'user': request.user,'post_comment':post_comment, 'comments': comments, 'comment_form': comment_form,'allcomments': allcomments,'future':future,'adv1':adv1,'adv2':adv2,'cat_r':remaining_categoreis,'value':value,'latest':latest, 'liked':liked,'is_bookmarked':is_bookmarked,'like_count':like_count}
    
    # merging both dictionaries
    # data_final = {**x_one,**data}
    data_final = data
    return render(request, 'blog/post.html', data_final)


# Category________________________________________________________________________________________________
def category(request, url):
    all_categories = Category.objects.all()
    first_4_categories = Category.objects.all()[0:4]
    remaining_categoreis = Category.objects.all()[::-1]
    cats = Category.objects.all()
    future = Past_events.objects.all()
    try:
        adv1 = Advertisement.objects.all()[0]
    except:
        adv1 = None
    try:
        adv2 = Advertisement.objects.all()[1::]
    except:
        adv2 = None
        
    # sidebar
    x_one = sidebar()

    cat = Category.objects.get(url=url)
    posts_ard = Post_with_image.objects.filter(category=cat)
    posts = posts_ard[3::]
    try:
        p1 = posts_ard[0:3]
        # print('p1',p1)
    except:
        p1 = None

    # comments = post.comments.filter(status=True)
    # allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data =  {'cat': cat,'cat_4': first_4_categories,'cat_r':remaining_categoreis, 'posts': posts,'p1':p1,'cats':cats,'future':future,'adv1':adv1,'adv2':adv2}
    
    # merging both dictionaries
    data_final = {**x_one,**data}
    return render(request, "blog/category.html",data_final)

# load more ________________________________________________________________________________________________
def load_more(request):    
    loaded_item = request.GET.get('loaded_item')    
    loaded_item_int = int(offset)    
    limit = 2    
    post_obj = list(Post_with_image().objects.values() [loaded_item_int:loaded_item_int+limit])    
    data = {'posts': post_obj}    
    return JsonResponse(data=data)




# search with new algorithm________________________________________________________________________________________________
def post_search(request):
    form = PostSearchForm()
    q = ''
    c = ''
    results = []
    query = Q()

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            c = form.cleaned_data['c']

            if c is not None:
                query &= Q(category=c)
            if q is not None:
                query &= Q(tags_for_seo_and_search_bar_in_website__contains=q)

            results = Post_with_image.objects.filter(query)
            # results = Question.objects.filter(query)

    return render(request, 'non_blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results})

# def search(request):
#     query=request.GET['query']
#     if len(query)>78:
#         allPosts=Post_with_image.objects.none()
#     else:
#         # allPostsTitle= Post_with_image.objects.filter(title__icontains=query)
#         # allPostsAuthor= Post_with_image.objects.filter(author__icontains=query)
#         # allPosts = list(chain(allPostsAuthor, allPostsTitle))

#         allPosts= Post_with_image.objects.filter(title__icontains=query)
#     if len(allPosts)==0:
#         messages.warning(request, "No search results found. Please refine your query.")
#     params={'allPosts': allPosts, 'query': query}
#     return render(request, 'search.html', params)

from non_blogs.models import Core_Team,Alumini_Team,Third_year_core_Team,Developer_Team,Web_content_management_Team

def about(request):
    #core team
    core_team = Core_Team.objects.all()
    amumini_team = Alumini_Team.objects.all()
    media_team = Third_year_core_Team.objects.all()
    dev_team = Developer_Team.objects.all()
    content_management_team = Web_content_management_Team.objects.all()

    context = {
        'core_team':core_team,
        'alumini_team':amumini_team,
        'media_team':media_team,
        'dev_team':dev_team,
        'content_management_team':content_management_team,
    }
    return render(request,'blog/about.html',context)

