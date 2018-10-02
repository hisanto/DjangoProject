from django.urls import path
from cryptoc.views import index, about, currencies, github, contact_us

urlpatterns = [
    path('', index, name='crypto_index'),
    path('about/', about, name='crypto_about'),
    path('currency/', currencies, name='crypto_currencies'),
    path('contact/', contact_us, name = 'crypto_contact'),
    path('github/', github, name='github'),
]
