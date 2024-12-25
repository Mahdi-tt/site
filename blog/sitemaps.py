from django.contrib.sitemaps import Sitemap
from .models import post

class blogSitemaps(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return post.objects.filter(status=True)

    def location(self,obj): 
        return obj.publish_date