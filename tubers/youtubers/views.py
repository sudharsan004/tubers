from django.shortcuts import render
from .models import Ytuber
from django.shortcuts import get_object_or_404
# Create your views here.


def youtubers(request):
    youtubers = Ytuber.objects.all()
    data = {
        'youtubers': youtubers
    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    youtuber = get_object_or_404(Ytuber, pk=id)
    data = {
        'youtuber': youtuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def youtubers_search(request):
    return render(request, 'base.html')
