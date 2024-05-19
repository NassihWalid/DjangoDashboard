# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Driver(models.Model):
    id_d = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def _str_(self):
        return self.name

class Road(models.Model):
    id_r = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ROAD_TYPES = (
        ('Auto-route', 'Auto-route'),
        ('National', 'National'),
        ('Rurale', 'Rurale'),
    )
    type = models.CharField(max_length=20, choices=ROAD_TYPES)

    def _str_(self):
        return self.name

class Vehicle(models.Model):
    id_v = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def _str_(self):
        return self.model

class Voyage(models.Model):
    id_vo = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='voyages')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='voyages')
    road = models.ForeignKey(Road, on_delete=models.CASCADE, related_name='voyages')
    datev = models.DateTimeField()

    def _str_(self):
        return f'Voyage on {self.datev} by {self.driver.name} with {self.vehicle.model} on {self.road.name}'

class Alert(models.Model):
    id_a = models.AutoField(primary_key=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='alerts')
    date = models.DateTimeField()

    def _str_(self):
        return f'Alert on {self.date} for Voyage {self.voyage.id_vo}'

