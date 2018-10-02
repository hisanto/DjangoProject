from django.shortcuts import render, redirect
from .models import Post  # models name

# Create your views here.


def articles(request):
    posts = Post.objects.all()
    ctx = {
        "posts": posts
    }
    return render(request,
                  template_name='blog/blog_index.html',
                  context=ctx)


def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        post = Post.objects.create(title=title, body=body, author=user, is_published=True)

        return redirect('blog_index')

    return render(request,
                  template_name='blog/blog_create.html',
                  context={}
                  )
