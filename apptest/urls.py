from django.urls import path
from apptest.views import *

urlpatterns = [
    path('', index_view, name = 'home' ),
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name = 'contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
    #path('coming-soon/', coming_soon, name='coming_soon'),
    #path('<path:anything>/', coming_soon, name='coming_soon_all'),



    
]
