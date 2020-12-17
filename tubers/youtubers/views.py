from django.shortcuts import render

# Create your views here.


def youtubers(request):
    return render(request, 'base.html')


def youtubers_detail(request, id):
    return render(request, 'base.html')


def youtubers_search(request):
    return render(request, 'base.html')
