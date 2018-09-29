from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('mine/', views.mine, name='mine'),
    path(r'user_list/', views.Blog_User_List.as_view()),
    path('user/<pk>/', views.Blog_User_Detail.as_view()),
    path(r'blog', views.BlogViews.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


