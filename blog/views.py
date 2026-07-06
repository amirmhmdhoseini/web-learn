from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_view(request):
    return render(request, 'blog-home.html')

def blog_single(request):
    context = {'title' : 'Dynamic Blog',
               'content': 'im just trying to make my first dynamic blog and im trying some new stuff :) ',
               'author' : 'amir mhmd'
               }
    return render(request, 'blog-single.html', context)
