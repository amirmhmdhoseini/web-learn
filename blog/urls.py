from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index' ),
    path('<int:pid>', blog_single, name = 'single' ),
    # path('post-<int:pid>', test_view, name = 'test'),
]

