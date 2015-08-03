from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class WallPost(models.Model):
    'This is a post that can be added by user and displayed on PostWall'
    pubdate = models.DateTimeField('date published')
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=50)

class User(models.Model):
    ''
    join_date = models.DateTimeField('join date')
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
