from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.


def login(request):
    return render(request, 'user_accounts/login.html')


# Django already has a build in logout method so give some other name to logout function
def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    return render(request, 'user_accounts/register.html')


def dashboard(request):
    return render(request, 'user_accounts/dashboard.html')
