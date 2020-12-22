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
    youtubers = Ytuber.objects.all()
    city_values = Ytubers.objects.values_list('city', flat=True)
    categorey_values = Ytubers.objects.values_list('categorey', flat=True)
    city_values = Ytubers.objects.values_list('city', flat=True)
    # for key in request.GET:
    #     if key == 'keyword':
    #         youtubers = youtubers.filter(
    #             description__icontains=request.GET[key])
    #     else:
    #         youtubers = youtubers.filter(
    #             =request.GET[key])

    # value = request.GET[key]
    # print(value)
    # if request.GET['keyword']:
    #     youtubers = youtubers.filter(
    #         description__icontains=request.GET['keyword'])
    # if request.GET['city']:
    #     youtubers = youtubers.filter(
    #         city__iexact=request.GET['city'])
    # if request.GET['categorey']:
    #     youtubers = youtubers.filter(
    #         categorey__iexact=request.GET['categorey'])
    # if request.GET['camera_type']:
    #     youtubers = youtubers.filter(
    #         city__iexact=request.GET['camera_type'])
    data = {'youtubers': youtubers, 'keyword': request.GET['keyword']}
    return render(request, 'youtubers/search.html', data)
