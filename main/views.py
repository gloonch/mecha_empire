from django.shortcuts import render
from .models import User
from django.http import JsonResponse, HttpResponse
import uuid


# Create your views here.

# first check if user's phone_number exists
def is_phone_number_registered(request):
    phone_number = request.GET.get('phone_number')
    if phone_number == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({
                'isRegistered': True, })
        else:
            return JsonResponse({
                'isRegistered': False, })


# gets phone_number and nickanme and registers the user
def generate_token(request):
    nickname = request.GET.get('nickname')
    phone_number = request.GET.get('phone_number')
    if nickname == "" and phone_number == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        # checks again if phone_number does not exits then try ...
        if User.objects.filter(phone_number=phone_number).exists() == False:
            try:
                generated_token = uuid.uuid1().hex
                user = User(nickname=nickname,
                            phone_number=phone_number,
                            token=generated_token)
                user.save()
                return JsonResponse(
                    {'token': generated_token,
                     'status': 200, }
                )
            except Exception as error:
                return JsonResponse(
                    {'status':500,
                     'error': error.__str__(), }
                )
        else:
            JsonResponse({
                'result': 'phone_number exists',
            })

    return JsonResponse({
        'status': 400,
    })
