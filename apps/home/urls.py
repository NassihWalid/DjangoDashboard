# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.Functions import RandomGenerators

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('generateRandomdriver/', RandomGenerators.generate_drivers_view, name='generate_drivers'),
    path('generateRandomroad/', RandomGenerators.generate_roads_view, name='generate_road'),
    path('generateRandomvehicule/', RandomGenerators.generate_vehicules_view, name='generate_vehicule'),
    path('generateRandomvoyage/', RandomGenerators.generate_voyages_view, name='generate_voyage'),
    path('generateRandomalert/', RandomGenerators.generate_alerts_view, name='generate_alert'),
    path('deletealert/', views.delete_all_alerts, name='delete_alert'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
