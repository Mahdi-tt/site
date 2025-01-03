
from django.contrib import sitemaps
from django.urls import reverse

class websitesitemaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"


    def items(self):
         return ["website:index", "website:contact"]
       

    def location(self, item):
        return reverse(item)