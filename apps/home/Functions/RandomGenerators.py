import string
import random
from datetime import datetime, timedelta
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import Driver, Road, Alert, Vehicle,Voyage




def generate_drivers_view(request):
    context = {}
    num_drivers = 20
    generate_and_insert_drivers(num_drivers, Driver)

    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))

def generate_random_driver():
    """Generates a random driver dictionary with name, phone, and email."""
    name_length = random.randint(5, 15)
    name = ''.join(random.choice(string.ascii_letters) for _ in range(name_length))

    phone_length = 10  # Adjust phone number length as needed
    phone = ''.join(random.choice(string.digits) for _ in range(phone_length))

    email = f"{name}@{random.choice(['gmail', 'yahoo', 'hotmail'])}.com"
    return {'name': name, 'phone': phone, 'email': email}

def generate_and_insert_drivers(num_drivers, model_class):
    """Generates and inserts random drivers into a provided model class.

    Args:
        num_drivers (int): Number of random drivers to generate.
        model_class (class): The Django model class representing a driver.
    """

    drivers_to_create = [model_class(**generate_random_driver()) for _ in range(num_drivers)]
    model_class.objects.bulk_create(drivers_to_create)

    return f"Successfully inserted {num_drivers} random drivers."

def generate_roads_view(request):
    context = {}
    num = 20
    generate_and_insert_roads(num, Road)

    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))
def generate_random_road():
    """Generates a random road dictionary with name and type."""
    name_length = random.randint(5, 15)
    name = ''.join(random.choice(string.ascii_letters) for _ in range(name_length))

    road_type = random.choice(['Auto-route', 'National', 'Rurale'])

    return {'name': name, 'type': road_type}


def generate_and_insert_roads(num_roads,model_class):
    """Generates and inserts random roads into a provided model class.

    Args:
        num_roads (int): Number of random roads to generate.
        model_class (class): The Django model class representing a road.
    """
    roads_to_create = [model_class(**generate_random_road()) for _ in range(num_roads)]
    model_class.objects.bulk_create(roads_to_create)

    return f"Successfully inserted {num_roads} random roads."

def generate_vehicules_view(request):
    context = {}
    num = 20
    generate_and_insert_vehicles(num, Vehicle)

    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))
def generate_random_vehicle():
    """Generates a random vehicle dictionary with model and year."""
    model_length = random.randint(5, 15)
    model = ''.join(random.choice(string.ascii_letters) for _ in range(model_length))

    year = random.randint(1990, 2023)  # Adjust the year range as needed

    return {'model': model, 'year': year}


def generate_and_insert_vehicles(num_vehicles, model_class):
    """Generates and inserts random vehicles into a provided model class.

    Args:
        num_vehicles (int): Number of random vehicles to generate.
        model_class (class): The Django model class representing a vehicle.
    """

    vehicles_to_create = [model_class(**generate_random_vehicle()) for _ in range(num_vehicles)]
    model_class.objects.bulk_create(vehicles_to_create)

    return f"Successfully inserted {num_vehicles} random vehicles."

def generate_voyages_view(request):
    context = {}
    num = 10
    generate_and_insert_voyages(num, Voyage)

    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))
def generate_random_voyage():
    """Generates a random voyage dictionary with vehicle, driver, road, and date."""
    vehicle = random.choice(Vehicle.objects.all())
    driver = random.choice(Driver.objects.all())
    road = random.choice(Road.objects.all())

    # Generate a random date within the past year
    datev = datetime.now() - timedelta(days=random.randint(0, 365))

    return {'vehicle': vehicle, 'driver': driver, 'road': road, 'datev': datev}


def generate_and_insert_voyages(num_voyages, model_class):
    """Generates and inserts random voyages into a provided model class.

    Args:
        num_voyages (int): Number of random voyages to generate.
        model_class (class): The Django model class representing a voyage.
    """

    voyages_to_create = [model_class(**generate_random_voyage()) for _ in range(num_voyages)]
    model_class.objects.bulk_create(voyages_to_create)

    return f"Successfully inserted {num_voyages} random voyages."


def generate_alerts_view(request):
    context = {}
    generate_and_insert_alerts( Alert)

    html_template = loader.get_template('home/page-500.html')
    return HttpResponse(html_template.render(context, request))
def generate_random_alert(voyage):
    """Generates a random alert for a given voyage with a random datetime."""
    # Generate a random datetime within the past year
    days_ago = random.randint(0, 365)
    random_time = timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    date = datetime.now() - timedelta(days=days_ago) - random_time
    return {'voyage': voyage, 'date': date}

def generate_and_insert_alerts(model_class):
    """Generates and inserts random alerts for all voyages.

    Args:
        model_class (class): The Django model class representing an alert.
    """
    voyages = Voyage.objects.all()
    alerts_to_create = []

    for voyage in voyages:
        num_alerts = random.choices(range(9), weights=[70, 10, 10, 10, 10, 10, 10, 5, 5])[0]
        for _ in range(num_alerts):
            alerts_to_create.append(model_class(**generate_random_alert(voyage)))

    model_class.objects.bulk_create(alerts_to_create)
    return f"Successfully inserted {len(alerts_to_create)} random alerts."