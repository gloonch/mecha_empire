from django.urls import path
from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('next_seven_days_event/', views.next_seven_days_event, name='next_seven_days_event'),
    path('filter_date/', views.filter_date, name='filter_date'),
]
