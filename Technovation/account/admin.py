from django.contrib import admin
from .models import Event_Type, Event, Profile, Participation
# Register your models here.

@admin.register(Event_Type)
class Event_TypeAdmin(admin.ModelAdmin):
    list_display=('event_type',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('event_name','event_type','summary')
    list_filter=('event_name','event_type',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','full_name','phone','college','year','payment_status')
    list_filter=('user','college','year','payment_status')

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display=('__str__','participant','event')
    list_filter=('participant','event')
