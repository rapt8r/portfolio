"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.http import FileResponse
from www.views import IndexPage, ContactPage, DownloadCVPage, AboutMePage, OpenGraphPage
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap
from django.conf import settings
sitemaps = {
    'static': StaticSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    #Files
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('opengraph.jpg', OpenGraphPage, name='opengraph'),
    path('', IndexPage.as_view(), name='index-page'),
    path('download-cv/', DownloadCVPage.as_view(), name='download-cv'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about-me/', AboutMePage.as_view(), name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
