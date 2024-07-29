from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50, unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)

class Hashtag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

class Discussion(models.Model):
    text_field = models.TextField()
    image = models.ImageField(upload_to='discussions/')
    hashtags = models.ManyToManyField(Hashtag, related_name='discussions')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
