from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from app.forms import BlogForms
from app.models import Blog_User, Blog, BlogSerializer
from app.serializers.serializer import Blog_UserSerializer


def login(request):
    return None


def register(request):
    if request.method == 'GET':
        return render(request, 'templates/html/register.html')
    username = request.POST.get('username', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    repeatpwd = request.POST.get('repeatpwd', None)
    icon = request.FILES.get('icon', None)
    if username and password and repeatpwd and email:
        if password==repeatpwd and not Blog_User.objects.filter(username=username):
            user = Blog_User()
            user.username = username
            user.password = password
            user.icon = icon
            user.save()
    return HttpResponse('注册成功，请登录邮箱并激活')


def logout(request):
    return None


def index(request):
    return None


def mine(request):
    return None


class Blog_User_List(generics.ListCreateAPIView):
    queryset = Blog_User.objects.all()
    serializer_class = Blog_UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Blog_User_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog_User.objects.all()
    serializer_class = Blog_UserSerializer

class BlogViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


def blog_edit(request):

    return render(request, 'templates/html/markdown.html')


def create(request):
    if request.method == "GET":
        form = BlogForms()
        return render(request, 'templates/html/blog_create.html', {'form':form})
    else:
        form = BlogForms(request.POST)
        if form.is_valid():
            blog_temp = Blog
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog_temp.title = title
            blog_temp.content = content
            blog_temp.save()
        return HttpResponse(content="Success!!")