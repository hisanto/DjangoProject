from django.urls import path
from cryptoc.views import index, aboutus, currencies, git_hub, contactus

urlpatterns = [
path('', index),
path('about/', aboutus),
path('contact/', contactus),
path('', currencies),
path('git/', git_hub),
]