from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('mine/', views.mine, name='mine'),
    path('user_list/', views.Blog_User_List),
    path('user/<pk>/', views.Blog_User_Detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)


