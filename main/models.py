from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField( max_length=100)
    banner = models.ImageField(upload_to='banner')
    intro = models.TextField()
    discription = models.TextField()
    iframe = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=15)
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Project(models.Model):
    title = models.CharField( max_length=100)
    banner = models.ImageField(upload_to='banner')
    intro = models.TextField()
    discription = models.TextField()
    iframe = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
class SocialLink(models.Model):
    linked_in=models.URLField(null=True, blank=True)
    github=models.URLField(null=True, blank=True)
    facebook=models.URLField(null=True, blank=True)
    discord=models.URLField(null=True, blank=True)
    instagram=models.URLField(null=True, blank=True)
    youtube=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True, blank=True)
    

class Resume(models.Model):
    resume = models.FileField(null=True, blank=True)
    


class Service(models.Model):
    icon = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

class Setup(models.Model):
    profile = models.ImageField()
