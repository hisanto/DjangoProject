from django.contrib import admin
from .models import Post, Comment  # added to display in admin url
admin.site.register(Post) # added to post in "http://localhost:8000/admin/"
admin.site.register(Comment)