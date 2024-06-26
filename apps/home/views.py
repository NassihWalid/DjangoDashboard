# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import string
import random
from datetime import datetime, timedelta
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Driver, Road, Alert, Vehicle,Voyage
from .Functions.Extraction import get_alerts_grouped_by_month, get_alerts_count_per_month,count_voyages_with_and_without_alerts





@login_required(login_url="/login/")
def index(request):

    context = {'segment': 'index'}
    context['driver_count'] = Driver.objects.count()
    context['road_count'] = Road.objects.count()
    context['alert_count'] = Alert.objects.count()
    context['vehicule_count'] = Vehicle.objects.count()
    context['voyage_count'] = Voyage.objects.count()
    context['alerts_count_grouped_by_month'] = get_alerts_count_per_month()
    context['count_voyages_with_alerts'] = count_voyages_with_and_without_alerts()[0]
    context['count_voyages_without_alerts'] = count_voyages_with_and_without_alerts()[1]
    context['percent_voyages_without_alerts'] = count_voyages_with_and_without_alerts()[0]/count_voyages_with_and_without_alerts()[0]+count_voyages_with_and_without_alerts()[1]
    context['drivers'] = list(Driver.objects.values_list('id_d', flat=True))

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def delete_all_alerts(request):
    Alert.objects.all().delete()
    return HttpResponse("All alerts have been deleted.")