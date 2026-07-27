from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index_view(request):
    
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

