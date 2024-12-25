from django import template
from django.utils import timezone
from blog.models import post
register = template.Library()

@register.inclusion_tag('website/website-lates-post.html')
def lates_post(arg=3):
    now = timezone.now()
    posts = post.objects.filter(status=1,publish_date__lte=now).order_by('-publish_date')[:arg]
    context = {'posts': posts}
    return context