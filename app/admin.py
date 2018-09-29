from django.contrib import admin
from app.models import Blog_User, Blog
# Register your models here.


class Blog_User_Admin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'icon', 'creation_time')
    list_per_page = 10
    list_filter = ('username',)
    ordering = ('id', )

admin.site.register(Blog_User, Blog_User_Admin)
admin.site.register(Blog)