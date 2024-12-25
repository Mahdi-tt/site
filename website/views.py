from django.shortcuts import render
from website.forms import contactForm
from django.contrib import messages
from blog.models import post
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'website/index.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            comit=form.save(commit= False)
            comit.name = 'unknown'
            comit.save()
            messages.success(request,'success message')
        else:
            messages.error(request,'Error contact')
    
    form = contactForm()
    context = {'form': form}    
    return render(request,'website/contact.html',context)

