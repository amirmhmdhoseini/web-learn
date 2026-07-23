from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag
def totalposts():
    posts = Post.objects.filter(is_published=True).count()
    return posts

@register.filter
def snippet (value, arg=20):
    return value[:arg]

@register.inclusion_tag('blog-latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(is_published = True).order_by('-published_date')[:arg]
    return {'posts' : posts}

@register.inclusion_tag('blog-category.html')
def post_categories():
    posts = Post.objects.filter(is_published = True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories' : cat_dict}