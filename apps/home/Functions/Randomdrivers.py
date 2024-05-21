import random
import string

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

    drivers_to_create = [generate_random_driver() for _ in range(num_drivers)]
    model_class.objects.bulk_create(drivers_to_create)

    return f"Successfully inserted {num_drivers} random drivers."

# Example Usage (assuming you have a view function in Functions.py)

