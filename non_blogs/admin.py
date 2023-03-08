from django.contrib import admin
from .models import Team, Value,Initiative, Advertisement,Future_events,Youtube_Video,Contact
from mptt.admin import MPTTModelAdmin
# Register your models here.

class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title2_like_how_we_do', 'title1_like_what_we_do', 'content1', 'date_of_initiative')
    search_fields = ('name',)
admin.site.register(Initiative,InitiativeAdmin)

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image')
    search_fields = ('name',)
admin.site.register(Advertisement,AdvertisementAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','subject','content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name','content','subject')

admin.site.register(Contact, ContactAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'quote','image')
    search_fields = ('name',)
admin.site.register(Team,TeamAdmin)

class ValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote','thumbnail')
    search_fields = ('name',)
admin.site.register(Value,ValueAdmin)

class Future_eventsAdmin(admin.ModelAdmin):
    list_display = ('title','date_of_event','month_of_event','any_hashtag')
admin.site.register(Future_events,Future_eventsAdmin)
# @admin.register(Contact)

from embed_video.admin import AdminVideoMixin


class AdminVideo(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Youtube_Video,AdminVideo)

