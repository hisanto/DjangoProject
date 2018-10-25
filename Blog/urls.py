from django.urls import path, include
from rest_framework import routers

from Blog.api import PostViewSet
from Blog.views import articles, create_article, blog_detail, add_comment, like_post, contact_us

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/', create_article, name='blog_create'),
    path('detail/<int:post_id>', blog_detail, name='blog_detail'),
    path('add-comment/', add_comment, name='add_comment'),
    path('like/<int:post_id>', like_post, name='like_post'),
    path('contact/', contact_us, name='contact')
]


# API ROUTER
router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns += [
    path('api/v1/', include(router.urls))
]
