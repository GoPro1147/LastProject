from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
# Create your views here.


def signup(request):
    if request.method == "POST":
            form = UserCustomCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
    else:
        form = UserCustomCreationForm()

    context={
        'form':form
    }
    return render(request,'accounts/form.html',context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movie_review:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'accounts/form.html',context)

def logout(request):
    auth_logout(request)
    return redirect('movie_review:index')

def user_info(request):
    if request.method == "POST":
        user_model = get_user_model()
        user_p = get_object_or_404(user_model, id=request.user.id)
        
        context = {
            'user_p':user_p
        }

        return render(request, 'accounts/user_info.html', context)