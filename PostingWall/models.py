from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class WallPost(models.Model):
    'This is a post that can be added by user and displayed on PostWall'
    pubdate = models.DateTimeField('date published')
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=50)