from django.contrib import admin
from .models import Map, Building, Floor, Room, Event
# Register your models here.
@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'map', 'description', 'picture')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('number', 'building', 'description', 'picture')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'description', 'picture')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'organizer', 'description', 'date', 'time', 'room')