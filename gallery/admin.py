from django.contrib import admin
from .models import GalleryImage

# Register your models here.

# admin.site.register(GalleryImage)


class GalleryImage_Admin(admin.ModelAdmin):
    list_display = ('id', 'image', 'tags')
    search_fields = ('tags',)
admin.site.register(GalleryImage,GalleryImage_Admin)