from django.shortcuts import render
from .models import User
from django.http import JsonResponse, HttpResponse

import secrets


# Create your views here.

def generate_token(request):
    nickname = request.GET.get('nickname')
    phone_number = request.GET.get('phone_number')

    if nickname == "" and phone_number == "":
        return JsonResponse({
            'status': 400
        })
    else:
        # User.objects.filter(phone_number=phone_number).exists()
        # return HttpResponse(type(User.objects.filter(phone_number=phone_number).exists()))
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'result': "phone number is already exist!"})
        if User.objects.filter(phone_number=phone_number).exists() == False:
            try:
                user = User()
                user.nickname = nickname
                user.phone_number = phone_number
                generated_token = secrets.token_hex()
                user.token = generated_token
                user.save()
                return JsonResponse(
                    {'token': generated_token,
                     'status': 200}
                )
            except:
                return JsonResponse(
                    {'status': 500}
                )
