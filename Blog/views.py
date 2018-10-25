from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from django.conf import settings

from .models import Post, Comments


def articles(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_date')

    ctx = {
        "posts": posts
    }

    return render(request,
                  template_name='blog/blog_index.html',
                  context=ctx)

@login_required
def create_article(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        post = Post.objects.create(title=title, body=body, author=user, is_published=True)

        return redirect(to='blog_index')

    return render(request,
                  template_name='blog/blog_create.html',
                  context={})

def blog_detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)
    post = Post.objects.filter(id=post_id).first()

    comments = Comments.objects.filter(post=post)

    ctx = {
        "post": post,
        "comments": comments
    }

    return render(request, template_name='blog/blog_detail.html', context=ctx)


@login_required
def add_comment(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        comment_body = request.POST.get("comment_body")
        post_id = request.POST.get("post_id")

        post = Post.objects.get(id=post_id)

        comment = Comments.objects.create(email=email,
                                          comment_body=comment_body,
                                          post=post)

        return redirect(to='blog_detail', post_id=post_id)


def like_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.num_likes += 1
        post.save()

        return JsonResponse({"new_likes_count": post.num_likes})


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        message = request.POST.get('message')

        ctx = {
            "name": name,
            "email": user_email,
            "message": message
        }

        template = get_template('blog/email_template.html')
        email_html = template.render(context=ctx)

        email = EmailMessage(
            'Someone sent you a message',
            email_html,
            "From My Blog",
            [settings.EMAIL_HOST_USER],
            headers={'Reply-To': user_email}
        )
        email.content_subtype = 'html'
        email.send()
        return redirect(to='contact')
    return render(request, template_name='blog/contact.html', context={})
