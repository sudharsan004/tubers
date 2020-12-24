from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name,
                                        email=email, password=password)
        user.save()
        messages.success(request, 'Account created')
        return redirect('login')
    return render(request, 'user_accounts/register.html')


def login(request):
    return render(request, 'user_accounts/login.html')


# Django already has a build in logout method so give some other name to logout function
def logout_user(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, 'user_accounts/dashboard.html')
