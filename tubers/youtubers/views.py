from django.shortcuts import render
from .models import Ytuber
from django.shortcuts import get_object_or_404
# Create your views here.


def youtubers(request):
    youtubers = Ytuber.objects.all()
    city_values = Ytuber.objects.values_list('city', flat=True).distinct()
    categorey_values = Ytuber.objects.values_list(
        'categorey', flat=True).distinct()
    camera_type = Ytuber.objects.values_list(
        'camera_type', flat=True).distinct()
    keyword = ''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        youtubers = youtubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        youtubers = youtubers.filter(city__iexact=city)
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        youtubers = youtubers.filter(camera_type__iexact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        youtubers = youtubers.filter(category__iexact=category)

    data = {'youtubers': youtubers, 'keyword': keyword, 'city_values': city_values,
            'categorey_values': categorey_values, 'camera_values': camera_type}
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    youtuber = get_object_or_404(Ytuber, pk=id)
    data = {
        'youtuber': youtuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def youtubers_search(request):
    youtubers = Ytuber.objects.all()
    city_values = Ytuber.objects.values_list('city', flat=True).distinct()
    categorey_values = Ytuber.objects.values_list(
        'categorey', flat=True).distinct()
    camera_type = Ytuber.objects.values_list(
        'camera_type', flat=True).distinct()
    keyword = ''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        youtubers = youtubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        youtubers = youtubers.filter(city__iexact=city)
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        youtubers = youtubers.filter(camera_type__iexact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        youtubers = youtubers.filter(category__iexact=category)

    data = {'youtubers': youtubers, 'keyword': keyword, 'city_values': city_values,
            'categorey_values': categorey_values, 'camera_values': camera_type}
    return render(request, 'youtubers/search.html', data)
