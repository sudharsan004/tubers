from django.shortcuts import render
from .models import Slider, TeamMember
# Create your views here.
from youtubers.models import Ytuber


def home(request):
    sliders = Slider.objects.all()
    team_members = TeamMember.objects.all()
    featured_ytubers = Ytuber.objects.order_by(
        '-created_at').filter(is_featured=True)
    ytubers = Ytuber.objects.order_by('-created_at')
    context = {'sliders': sliders,
               'team_members': team_members, 'ytubers': ytubers, 'featured_ytubers': featured_ytubers}
    return render(request, 'webpages/home.html', context)


def services(request):
    return render(request, 'webpages/services.html')


def about(request):
    team_members = TeamMember.objects.all()
    data = {'team_members': team_members}
    return render(request, 'webpages/about.html', data)


def contact(request):
    return render(request, 'webpages/contact.html')
