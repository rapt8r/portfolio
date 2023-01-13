from django.contrib import sitemaps
from django.urls import reverse

class StaticSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['index-page', 'download-cv', 'contact']

    def location(self, item):
        return reverse(item)