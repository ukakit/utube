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
    
    def add_view(self):
        self.view += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']