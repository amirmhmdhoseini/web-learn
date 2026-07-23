from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(is_published = 1,
                                published_date__lte=timezone.now())
    context = {'posts' : posts}
    return render(request, 'blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(
        Post,
        id=pid,
        is_published=True,
        published_date__lte=timezone.now()
    )

    all_posts = list(
        Post.objects.filter(
            is_published=True,
            published_date__lte=timezone.now()
        ).order_by('published_date')
    )

    current_index = all_posts.index(post)

    previous_post = None
    next_post = None

    if current_index > 0:
        previous_post = all_posts[current_index - 1]

    if current_index < len(all_posts) - 1:
        next_post = all_posts[current_index + 1]

    post.counted_views += 1
    post.save()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'blog-single.html', context)

def test_view(request):
    posts = Post.objects.all
    context = {'posts' : posts}
    return render(request, 'test.html', context)
