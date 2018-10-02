from django.urls import path

from blog.views import articles, create_article

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/', create_article, name='blog_create')
]
