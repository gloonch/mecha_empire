from django.contrib import admin
from .models import Event, Robot, Nation, Mode


# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('start_time', 'end_time', 'is_private', 'result')
        }),
        ('Advanced options', {
            'classes': ('mode',),
            'fields': ('mode', 'team_nations', 'robot_to_users'),
        }),
    )

@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    pass

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    pass

@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    pass