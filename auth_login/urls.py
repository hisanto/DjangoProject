from django.urls import path

from auth_login.views import loginForm, login_user, logout_user

urlpatterns=[
    path('login/',loginForm,name='login_form'),
    path('login-user/',login_user, name='login_user'),
    path('logout-user/',logout_user, name='logout_user'),
]