from django.shortcuts import render
from .models import Slider
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    return render(request, 'webpages/home.html', context={'sliders': sliders})


def services(request):
    return render(request, 'webpages/dashboard.html')


def about(request):
    return render(request, 'admin/base_site.html')


def contact(request):
    return render(request, 'admin/base_site.html')
