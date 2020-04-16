from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    return JsonResponse({'status': 200})


def create_event(request):
    # TODO
    return JsonResponse({'result': 200})


def next_seven_days_event(request):
    # TODO
    return JsonResponse({'result': 200})

def filter_date():
    # depends on DateField
    pass