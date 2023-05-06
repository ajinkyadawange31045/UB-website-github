from django.contrib import admin
from .models import  Value,Initiative, Advertisement,Past_events,Youtube_Video,Contact,Core_Team,Alumini_Team,Developer_Team,Third_year_core_Team,Web_content_management_Team
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


class ValueAdmin(admin.ModelAdmin):
    list_display = ('name','quote', 'thumbnail')
    search_fields = ('name',)
admin.site.register(Value,ValueAdmin)

class Past_eventsAdmin(admin.ModelAdmin):
    list_display = ('title','date_of_event','month_of_event','any_hashtag')
admin.site.register(Past_events,Past_eventsAdmin)
# @admin.register(Contact)

from embed_video.admin import AdminVideoMixin


class AdminVideo(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Youtube_Video,AdminVideo)






class Alumini_TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
admin.site.register(Alumini_Team,Alumini_TeamAdmin)

class Core_TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'image')
    search_fields = ('name',)
admin.site.register(Core_Team,Core_TeamAdmin)

class Third_year_core_TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'image')
    search_fields = ('name',)
admin.site.register(Third_year_core_Team,Third_year_core_TeamAdmin)

class Developer_TeamAdmin(admin.ModelAdmin):
    list_display = ('name',  'image')
    search_fields = ('name',)
admin.site.register(Developer_Team,Developer_TeamAdmin)

class Web_content_management_TeamAdmin(admin.ModelAdmin):
    list_display = ('name',  'image')
    search_fields = ('name',)
admin.site.register(Web_content_management_Team,Web_content_management_TeamAdmin)

