from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()

#Model to templete bridge
@register.simple_tag
def post_count():
    return Post.objects.count()

@register.inclusion_tag("blog/latest_posts.html")
def get_latest(count = 3):
    latest_post = Post.objects.order_by("-published_date")[:count]
    return {"latest_post" : latest_post}

@register.simple_tag
def get_popular(count=3):
    return Post.objects.annotate(total_comment = Count('comments')).order_by('-total_comment')[:count]

@register.filter(name='my_filter')
def to_upper(text):
    return text.upper()