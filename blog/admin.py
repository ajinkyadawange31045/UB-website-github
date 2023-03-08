from django.contrib import admin
from .models import Category, Author, Author, Post_with_image,Comment
from mptt.admin import MPTTModelAdmin

# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class Post_with_imageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('category','blog_views',)
    readonly_fields = ('blog_views',)
    class Media:
            js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)
    # list_per_page = 50

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','image')
    search_fields = ('name',)




class MPTTModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'publish', 'status')
    list_filter = ('post', 'name')
    search_fields = ('name','content')

admin.site.register(Comment, MPTTModelAdmin)


admin.site.register(Author,AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post_with_image, Post_with_imageAdmin)

from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

class MyGroupAdmin(GroupAdmin):
    def get_form(self, request, obj=None, **kwargs):
        # Get form from original GroupAdmin.
        form = super(MyGroupAdmin, self).get_form(request, obj, **kwargs)
        if 'permissions' in form.base_fields:
            permissions = form.base_fields['permissions']
            permissions.queryset = permissions.queryset.exclude(content_type__app_label__in=['admin', 'auth']) # Example
        return form



############ ADD THIS #############
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)
###################################



from typing import Set

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
admin.site.unregister(User)
# @admin.register(User)
class CustomUserAdmin(UserAdmin):
    def has_delete_permission(self, request, obj=None):
        if obj is None:
           return True
        else:
           return not obj.is_superuser
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                # 'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
admin.site.register(User, CustomUserAdmin)


from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied