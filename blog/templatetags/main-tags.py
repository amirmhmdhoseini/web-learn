from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('latest_posts.html')
def latest_posts():
    posts = Post.objects.filter(is_published=True,
                                published_date__lte=timezone.now()).order_by('-published_date')[:6]
    context = {'posts' : posts}
    return context