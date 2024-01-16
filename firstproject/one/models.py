from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(upload_to='song')
    year = models.IntegerField()
    music = models.CharField(max_length=200)
    director =models.CharField(max_length=200)
    Language = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio',blank=' ')

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(blank=True,max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300,default="",null=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    username = models.CharField(max_length=100)
    stars = models.IntegerField()
    reviews = models.TextField()

    def __str__(self):
        return self.username  


