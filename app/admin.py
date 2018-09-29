from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

from app.models import Blog_User, Blog
# Register your models here.


class Blog_User_Admin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'icon', 'creation_time')
    list_per_page = 10
    list_filter = ('username',)
    ordering = ('id', )

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':MDEditorWidget}
    }

admin.site.register(Blog_User, Blog_User_Admin)
admin.site.register(Blog, BlogAdmin)