from django.shortcuts import render
from blog.models import post ,comment
from django.utils import timezone
from blog.forms import commentforms
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger
from django.shortcuts import redirect
# Create your views here.
def blog_single(request,id):
    if request.method =='POST':
        form = commentforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'success comment')
        else:
            messages.error(request,form.errors.as_text())
    form = commentforms()
    now = timezone.now()
    posts = get_object_or_404(post,pk=id,status=1,publish_date__lte=now)
    posts.cuntent_view +=1
    posts.save()
    comments = comment.objects.filter(aproved = True,post=posts.id) 
    context = {'posts': posts,
               'form':form,
               'comment':comments}
    return render(request,'blog/blog-single.html',context)

def blog_home(request,cat_name=None):
    now = timezone.now()
    posts = post.objects.filter(status=1,publish_date__lte=now)
    paginators = Paginator(posts,3)
    page_number = request.GET.get('page')
    if cat_name:
        posts = posts.filter(categore__name=cat_name)
        
    try:
        posts = paginators.get_page(page_number)
    except EmptyPage:
        posts = paginators.get_page(1)
    except PageNotAnInteger:
        posts = paginators.get_page(1)

    context = {'post': posts}
    return render(request,'blog/blog_home.html',context)

def search(request):
    now = timezone.now()
    if request.method == 'GET':
        posts= post.objects.filter(status=1,publish_date__lte=now)
        if s:=request.GET.get('search'):
            posts=posts.filter(content__contains=s) or posts.filter(titel__contains=s)

    context = {'post':posts}
    return render(request,'blog/blog_home.html',context)

def page_not_found(request, exception):
    return render(request,'404.html',status=404)
        