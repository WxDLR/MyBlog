from django.contrib import auth
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from mdeditor.fields import MDTextField
from rest_framework import serializers

# Create your models here.
class Blog_User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=40, null=False)
    icon = models.ImageField(default='/templates/icon/defaulticon.jpg')
    creation_time = models.DateTimeField(auto_now_add=True,)


    # class Meta:
    #     db_table = 'blog_user'
    #     ordering = ('creation_time',)


class Blog(models.Model):
    title = models.CharField(max_length=40)
    content = MDTextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'content' )