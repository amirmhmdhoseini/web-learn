from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apptest.models import Contact

# Create your views here.

def blog_view(request, cat_name=None, author_username = None):
    posts = Post.objects.filter(is_published = 1,
                                published_date__lte=timezone.now())
    if cat_name != None:
        posts = posts.filter(category__name=cat_name)

    if author_username != None:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
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
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()

    return render(request, 'test.html')

def blog_category(request, cat_name):
    posts = Post.objects.filter(is_published=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts' : posts}
    return render(request, 'blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(is_published = 1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts' : posts}
    return render(request, 'blog-home.html', context)