from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap #this
from blog.sitemaps import PostSitemap #this
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)