from django.db import models
import time
from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    thumbnail = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body