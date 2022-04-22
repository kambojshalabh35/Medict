from django.db import models

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    metadesc = models.CharField(max_length=150)
    content = models.TextField()
    thumbimg = models.ImageField(upload_to='blogs/thumbnail', blank=True, null=True)
    featureimg = models.ImageField(upload_to='blogs/', blank=True, null=True)
    tags = models.TextField()
    dateposted = models.DateField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()