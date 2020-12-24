from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'user_accounts/login.html')


# Django already has a build in logout method so give some other name to logout function
def logout_user(request):
    return render(request, 'webpages/home.html')


def register(request):
    return render(request, 'user_accounts/register.html')


def dashboard(request):
    return render(request, 'user_accounts/dashboard.html')
