# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Driver, Road, Vehicle, Voyage, Alert

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id_d', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('id_r', 'name', 'type')
    search_fields = ('name',)
    list_filter = ('type',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id_v', 'model', 'year')
    search_fields = ('model',)
    list_filter = ('year',)

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display = ('id_vo', 'vehicle', 'driver', 'road', 'datev')
    search_fields = ('vehicle__model', 'driver__name', 'road__name')
    list_filter = ('datev', 'vehicle__model', 'driver__name', 'road__type')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('id_a', 'voyage', 'date')
    search_fields = ('voyage__id_vo',)
    list_filter = ('date',)