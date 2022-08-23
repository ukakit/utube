from django.contrib import admin
from .models import Video, Comment, Thumbnail, Media
# Register your models here.

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Thumbnail)
admin.site.register(Media)