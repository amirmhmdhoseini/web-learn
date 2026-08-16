from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from apptest.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from debug_toolbar.toolbar import debug_toolbar_urls
from apptest import views


sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap
}


urlpatterns = [
    #path('', views.coming_soon),
    #path('<path:anything>', views.coming_soon),
    path('admin/', admin.site.urls),
    path('', include('apptest.urls')),
    path('blog/', include('blog.urls')),
    path("sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('accounts.urls')),

    
]
urlpatterns += debug_toolbar_urls()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
