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
    list_display = ('id','title', 'topic', 'author', 'views',)
    search_fields = ('topic', 'author', 'title')
    sortable_by = ('topic',)
    list_filter = ('topic','author',)
    readonly_fields = ('likes_count','views')
admin.site.register(Post,Post_Admin)

# @admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    list_display = ('author','id', 'post','body')
    search_fields = ('post','author','body')
    list_filter = ('post','author')
admin.site.register(Comment,Comment_Admin)