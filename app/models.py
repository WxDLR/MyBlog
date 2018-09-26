from django.db import models

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


