from django.contrib import admin
from .models import Event, Robot, Nation, Mode


# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
