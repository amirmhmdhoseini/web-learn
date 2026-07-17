from django.urls import path
from apptest.views import *

urlpatterns = [
    path('', index_view, name = 'home' ),
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name = 'contact'),

    
]
