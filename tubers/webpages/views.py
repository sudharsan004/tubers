from django.shortcuts import render
from .models import Slider, TeamMember
# Create your views here.
from youtubers.models import Ytuber


def home(request):
    sliders = Slider.objects.all()
    team_members = TeamMember.objects.all()
    ytubers = Ytuber.objects.order_by('-created_at').filter(is_featured=True)
    context = {'sliders': sliders,
               'team_members': team_members, 'featured_ytubers': ytubers}
    return render(request, 'webpages/home.html', context)


def services(request):
    return render(request, 'webpages/dashboard.html')


def about(request):
    return render(request, 'admin/base_site.html')


def contact(request):
    return render(request, 'admin/base_site.html')
