from django.shortcuts import render, reverse,HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.db.models import Sum
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from crispy_forms.helper import FormHelper

from .models import Topic, Post, Comment
from .forms import CreateCommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
# from .forms import MyForm

# def my_view(request):
#     form = MyForm()
#     context = {'form': form}
#     return render(request, 'my_template.html', context)

# Topic views
@login_required
def like_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('forum:post-detail', args=[str(post.pk)]))




from django.db.models import Sum

class TopicListView(ListView):
    model = Topic
    template_name = 'forum/index.html'
    context_object_name = 'topics'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            queryset = queryset.filter(title__icontains=search_input)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_input'] = self.request.GET.get('search-area') or ''
        
        # Get the total views of all posts
        total_views = Post.objects.aggregate(Sum('views'))['views__sum']

        Post.objects.annotate(total_views=Sum('views'))
        value = str(total_views)
        if value.isdigit():
            value_int = int(value)
            if value_int > 1000000:
                value = "%.1f%s" % (value_int/1000000.00, 'M')
            else:
                if value_int > 1000:
                    value = "%.1f%s" % (value_int/1000.0, 'k')
    
        context['total_views'] = value
        
        # Get the total number of posts
        total_posts = Post.objects.count()
        context['total_posts'] = total_posts
        
        # Get the total number of likes
        total_likes = Post.objects.aggregate(Sum('likes'))['likes__sum']
        context['total_likes'] = total_likes
        
        return context

class TopicDetailView(LoginRequiredMixin,DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        posts = Post.objects.filter(topic=self.kwargs.get('pk'))
        context['posts'] = posts
        context['total_posts'] = posts.filter(author=self.request.user).count()
        return context

from django.urls import reverse_lazy

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']
    success_url = reverse_lazy('forum:forum-index')  # add this line

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url



# Post views
class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    form_class = CreateCommentForm
    
    def get_object(self):
        post = super().get_object()

        
        #this will have unique number of view for every loggedin user. and views will not be counted if the user is logged out
        
        # session = SessionStore(session_key=self.request.session.session_key)
        # viewed_posts = session.get('viewed_posts', [])
        # if post.id not in viewed_posts:
        #     post.views += 1
        #     post.save()
        #     viewed_posts.append(post.id)
        #     session['viewed_posts'] = viewed_posts
        #     session.save()



        #it will simply increase count on every refresh.
        viewed_posts =[]
        post.views += 1
        post.save()
        viewed_posts.append(post.id)
        

        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs.get('pk'), parent = None)
        context['form'] = CreateCommentForm(initial={'post': self.object, 'author': self.request.user})

        something = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = something.total_likes()
        liked = False
        if something.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


    def get_success_url(self):
        return reverse('forum:post-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

# Static pages

def login(request):
    return render(request, 'forum/login.html')

def logout(request):
    return render(request, 'forum/logout.html')

@login_required
def nested_comment(request, id) :
    if request.method == "POST" :
        get_comment = Comment.objects.get(id = id)
        if get_comment :
            get_post = get_comment.post
            get_body = request.POST["nested_comment"]
            nested_comment = Comment(
                author = request.user,
                post = get_post,
                body = get_body,
                parent = get_comment
            )
            nested_comment.save()
            return HttpResponseRedirect(reverse('forum:post-detail', args=[str(get_post.pk)]))

