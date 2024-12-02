written in python on pydroid3
made by x0loft


import random
from geopy.geocoders import Nominatim

# Set the number of entries to generate
num_entries_to_generate = 10

def generate_realistic_addresses(num_addresses):
    geolocator = Nominatim(user_agent="address_generator")

    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    last_names = ['Smith', 'Johnson', 'Garcia', 'Brown', 'Lee']

    fake_data = []
    for _ in range(num_addresses):
        # Generate a random name
        name = random.choice(first_names) + ' ' + random.choice(last_names)

        # Generate a random age
        age = random.randint(18, 80)

        # Generate a random phone number
        phone_number = '555-' + str(random.randint(100, 999)) + '-' + str(random.randint(1000, 9999))

        # Generate a random email address
        email = name.lower().replace(' ', '.') + '@gmail.com'

        # Generate random coordinates (latitude and longitude)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Reverse geocode the coordinates to get address information
        location = geolocator.reverse((latitude, longitude), language='en')

        # Check if location is valid and has address information
        if location is not None and 'address' in location.raw:
            address = {
                "country": location.raw['address'].get("country", ""),
                "city": location.raw['address'].get("city", ""),
                "state": location.raw['address'].get("state", "")
            }

            # Append generated data to the list
            fake_data.append({
                "name": name,
                "age": age,
                "phone_number": phone_number,
                "email": email,
                "address": address
            })

    return fake_data

# Example usage:
fake_entries = generate_realistic_addresses(num_entries_to_generate)

for entry in fake_entries:
    print('Name:', entry["name"])
    print('Age:', entry["age"])
    print('Phone Number:', entry["phone_number"])
    print('Email:', entry["email"])
    print('Address:', entry["address"])
    print('\n')
