# -*- coding:utf-8 -*-
from rest_framework import serializers
from app.models import Blog_User

class Blog_UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog_User
        fields = ('id', 'username', 'password', 'email', 'icon', 'creation_time')


