from django.urls import path
from apptest.views import *

urlpatterns = [
    path('', index_view, name = 'home' ),
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name = 'contact'),
    path('blog-single/', blog_single_view, name = 'blog-single'),
    path('blog-home/', blog_home_view, name = 'blog-home'),
]
