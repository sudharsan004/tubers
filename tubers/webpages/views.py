from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'webpages/home.html')


def services(request):
    return render(request, 'webpages/dashboard.html')


def about(request):
    return render(request, 'admin/base_site.html')


def contact(request):
    return render(request, 'admin/base_site.html')
