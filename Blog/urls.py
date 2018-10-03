from django.urls import path

from blog.views import articles, create_article, blog_detail

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/', create_article, name='blog_create'),
    path('detail/<int:post_id>', blog_detail, name='blog_detail'),
]
