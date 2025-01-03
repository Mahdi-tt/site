"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import blogSitemaps
from website.sitemaps import websitesitemaps
from debug_toolbar.toolbar import debug_toolbar_urls
from django.views.generic import TemplateView


sitemaps = {
    "static": websitesitemaps,
    "blog" : blogSitemaps
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), 
    path('blog/', include('blog.urls')), 
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', include('robots.urls')),

]+ debug_toolbar_urls()

handler404 = 'blog.views.page_not_found'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
