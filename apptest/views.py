from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from blog.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.SUCCESS, 'Success!')
                contact = form.save(commit=False)
                contact.name = "Unknown"
                contact.save()
                return HttpResponseRedirect('/contact/')
            else:
                 messages.add_message(request, messages.ERROR, 'Failed :(')
    else:
         form = ContactForm()
    return render(request, 'contact.html', {'form': form})

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
          
     
