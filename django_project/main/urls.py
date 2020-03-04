from django.urls import path
from . import views

urlpatterns = [
    path('generate_token/', views.generate_token, name='generate_token'),
    path('is_phone_number_registered/', views.is_phone_number_registered, name='is_phone_number_registered'),
]