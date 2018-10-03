from django.urls import path

from Blog.views import articles, create_article, blog_detail, article_comment

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/', create_article, name='blog_create'),
    path('comment/', article_comment, name='blog_comment'),
    path('detail/<int:post_id>', blog_detail, name='blog_detail'),
]
