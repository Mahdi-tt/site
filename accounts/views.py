from django.shortcuts import render
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import customUserCreationForm
# Create your views here.
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST' :
            login_input = request.POST.get('username')
            password = request.POST.get('password')
            if "@" in login_input:
                user_obj = User.objects.filter(email = login_input).first()
            else:
                user_obj = User.objects.filter(username = login_input).first()
            if user_obj:
                user = authenticate(request,username = user_obj.username,  password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request,'login successful')
                    return redirect('/')
                else:
                    messages.error(request,'username or password not join')
            else:
                messages.error(request,'username or password')
    else:
        messages.error(request,'you are login ')
        return redirect('/')
    return render(request,'account/login.html')


def singup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST' :
            form =  customUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'signup successful')
                return redirect('/account/login/')
            else:
                messages.error(request,form.errors.as_text())
    else:
        messages.error(request,'you are login ')
        return redirect('/')
    form =  customUserCreationForm
    context = {'form':form}
    return render(request,'account/singup.html',context)



@login_required(login_url='/account/login/')
def logout_view(request):
    logout(request)
    return redirect('/')