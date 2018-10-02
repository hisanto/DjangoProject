from django.urls import path
from cryptoc.views import index, about, currencies, github, contactus

urlpatterns = [
    path('', index, name='crypto_index'),
    path('about/', about, name='crypto_about'),
    path('crypto/', currencies, name='crypto_currencies'),
    path('contactus/', contactus, name = 'crypto_contact'),
    path('github/', github, name='github'),
]
