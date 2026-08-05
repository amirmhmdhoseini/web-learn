from django.urls import path
from . import views

appname = 'accounts'

urlpatterns = [

    path('login', views.login_view, name='login'),
    # logout
    path('signup', views.signup_view, name='signup'),

]