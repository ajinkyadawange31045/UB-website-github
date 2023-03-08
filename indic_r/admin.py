from django.contrib import admin
from .models import Competition, Workshop, Talk, Proshow, SocialInitiative, EntityComment,Sponsor

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('id', 'speaker_name')

@admin.register(Proshow)
class ProshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(SocialInitiative)
class SocialInitiativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Sponsor)
class SocialInitiativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(EntityComment)
class EntityCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'likes', 'competition', 'workshop', 'talk', 'proshow', 'social_initiative')
    list_filter = ('competition', 'workshop', 'talk', 'proshow', 'social_initiative')
