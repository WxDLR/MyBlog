from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import Response, Request
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


from app.models import Blog_User
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

class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def blog_user_list(request):
#     if request.method == 'GET':
#         blog_user = Blog_User.objects.all()
#         serializer = Blog_UserSerializer(blog_user, many=True)
#         return JsonResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = Blog_UserSerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def blog_user_details(request, pk):
#     try:
#         blog_user = Blog_User.objects.get(pk=pk,)
#     except Blog_User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         blog_user = Blog_UserSerializer(blog_user)
#         return JsonResponse(blog_user.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Blog_UserSerializer(blog_user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         blog_user.delete()
#         return HttpResponse(status=204)


# @api_view(['GET', 'POST'])
# def user_list(request, format=None):
#     if request.method == 'GET':
#         userlist = Blog_User.objects.all()
#         serializer = Blog_UserSerializer(userlist, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = Blog_UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_details(request, pk, format=None):
#     try:
#         blog_user = Blog_User.objects.get(pk=pk,)
#     except Blog_User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         blog_user = Blog_UserSerializer(blog_user)
#         return Response(blog_user.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Blog_UserSerializer(blog_user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         blog_user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class Blog_User_List(generics.ListCreateAPIView):
    queryset = Blog_User.objects.all()
    serializer_class = Blog_UserSerializer


class Blog_User_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog_User.objects.all()
    serializer_class = Blog_UserSerializer