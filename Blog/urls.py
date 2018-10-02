from django.urls import path
from Blog.views import articles

urlpatterns = [
    path('blog/',articles),
]