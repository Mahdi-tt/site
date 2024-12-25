from django import template

register = template.Library()
@register.filter(name='short')
def function(value,arg=20):
    return value[:arg]+'...'
# @register.inclusion_tag('blog/blog-newsletter.html')
# def newlatters(request):
#     if request.method =='POST':
#         form = newsletter(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'success Newsletter')
#         else:
#             messages(request,'errorNewsletter')