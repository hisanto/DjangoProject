from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginForm(request):
    if request.user.is_authenticated:
        return redirect('blog_index')
    else:
        return  render(request, template_name='auth_login/login.html')

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return redirect('blog_index')
    else:
        return redirect('login_form')

def logout_user(request):
    logout(request)
    return redirect('blog_index')
