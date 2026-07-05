from django.urls import path
from apptest.views import *

urlpatterns = [
    path('', index_view ),
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog-single/', blog_single_view),
    path('blog-home/', blog_home_view),
]
