from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(is_published = 1)
    context = {'posts' : posts}
    return render(request, 'blog-home.html', context)

def blog_single(request):
    context = {'title' : 'Dynamic Blog',
               'content': 'im just trying to make my first dynamic blog and im trying some new stuff :) ',
               'author' : 'amir mhmd'
               }
    return render(request, 'blog-single.html', context)

def test_view(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'test.html', context)
