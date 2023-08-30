from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    
class Post(models.Model):
    title=models.TextField(max_length=200)
    content=models.TextField(max_length=1000)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    date=models.DateTimeField(auto_now=True)
    

    