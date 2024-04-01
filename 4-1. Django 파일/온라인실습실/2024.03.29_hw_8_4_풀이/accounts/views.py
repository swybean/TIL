from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User


# Create your views here.
def index(request):
    accounts = User.objects.all()
    context = {
        'accounts': accounts,
    }
    return render(request, 'accounts/index.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
        
    else:
        form =  AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(requset):
    auth_logout(requset)
    return redirect('accounts:index')


