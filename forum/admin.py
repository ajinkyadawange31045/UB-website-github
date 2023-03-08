from django.contrib import admin
from .models import Topic, Post, Comment

# admin.site.register(Topic)
# admin.site.register(Post)
# admin.site.register(Comment)



class Topic_Admin(admin.ModelAdmin):
    list_display = ('id', 'title','description')
admin.site.register(Topic,Topic_Admin)

# @admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'author', 'likes_count',)
    search_fields = ('topic', 'author', 'title')
    sortable_by = ('topic',)
admin.site.register(Post,Post_Admin)

# @admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    list_display = ('id', 'post','author','body')
    search_fields = ('post','author')
admin.site.register(Comment,Comment_Admin)