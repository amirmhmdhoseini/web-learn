from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from blog.forms import ContactForm, NewsletterForm

def index_view(request):
    
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    else:
         form = ContactForm()
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def newsletter_view(request):
    if request.method == "POST":
          form = NewsletterForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect("/")

    else:
         return HttpResponseRedirect('/')
          
     
