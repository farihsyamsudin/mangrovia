from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from websites.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai_app.urls')),
    path('', landing_page, name='landing_page'),
    path('berita/', berita_page, name='page_berita'),
    path('mangrove-wikipedia', mang_wiki, name="mang_wiki"),
    path('tentang/', about, name="about"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)