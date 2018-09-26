# -*- coding:utf-8 -*-
from rest_framework import serializers
from app.models import Blog_User

# class Blog_UserSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(required=True, max_length=20)
#     password = serializers.CharField(required=True, )
#     email = serializers.EmailField(required=False)
#     icon = serializers.ImageField(required=False)
#     creation_time = serializers.DateTimeField(required=False)
#
#     def create(self, validated_data):
#         return Blog_User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)
#         instance.icon = validated_data.get('icon', instance.icon)
#         instance.creation_time = validated_data.get('creation_time', instance.creation_time)
#         instance.save()
#         return instance

class Blog_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_User
        fields = ('id', 'username', 'password', 'email', 'icon', 'creation_time')
