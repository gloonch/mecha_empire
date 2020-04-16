from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Event, Mode, Nation, Robot

# Create your views here.
@method_decorator(csrf_exempt)
def create_event(request):
    # this should be a zero or one value (int)
    is_private = request.GET.get('is_private')
    # id of existing game modes (int)
    mode = request.GET.get('mode')
    # id of existing nations (int)
    team_nations_a = request.GET.get('team_nations_a')
    team_nations_b = request.GET.get('team_nations_b')
    # id of existing robots (int)
    robot_to_users_a = request.GET.get('robot_to_users_a')
    robot_to_users_b = request.GET.get('robot_to_users_b')

    if mode == "" and team_nations_a == "" and \
            team_nations_b == "" and robot_to_users_b == "" and robot_to_users_a == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        try:
            event = Event(is_private=is_private, mode=Mode.objects.get(pk=mode))
            event.save()
            event.team_nations.add(Nation.objects.get(pk=team_nations_a))
            event.team_nations.add(Nation.objects.get(pk=team_nations_b))
            event.robot_to_users.add(Robot.objects.get(pk=robot_to_users_a))
            event.robot_to_users.add(Robot.objects.get(pk=robot_to_users_b))

            return JsonResponse({
                'result': 200,
            })
        except Exception as err:
            return JsonResponse({
                'result': 500,
                'error': err.__str__(),
            })


def next_seven_days_event(request):
    # TODO
    return JsonResponse({'result': 200})


def filter_date():
    # depends on DateField
    pass
