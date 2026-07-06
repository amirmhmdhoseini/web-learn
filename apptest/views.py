from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def test_view(request):
    return render(request, 'test.html')
