from django.shortcuts import render
from .models import Slider, TeamMember
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    team_members = TeamMember.objects.all()
    context = {'sliders': sliders, 'team_members': team_members}
    return render(request, 'webpages/home.html', context)


def services(request):
    return render(request, 'webpages/dashboard.html')


def about(request):
    return render(request, 'admin/base_site.html')


def contact(request):
    return render(request, 'admin/base_site.html')
