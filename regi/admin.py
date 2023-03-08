from django.contrib import admin
from .models import Profile,User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number',)
    search_fields = ('username',)

admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Profile)
