written in python
made by x0loft

import random

# Set the number of entries to generate
num_entries_to_generate = 10

def generate_realistic_addresses(num_addresses):
    first_names = ['alice', 'bob', 'charlie']
    last_names = ['smith', 'johnson', 'garcia']
    fake_data = []

    # Predefined list of locations with their coordinates
    locations = [
        {"latitude": 37.7749, "longitude": -122.4194, "city": "San Francisco", "state": "CA"},
        {"latitude": 40.7128, "longitude": -74.0060, "city": "New York", "state": "NY"},
        {"latitude": 34.0522, "longitude": -118.2437, "city": "Los Angeles", "state": "CA"},
        # Add more locations as needed
    ]

    for _ in range(num_addresses):
        # generate a random name
        name = random.choice(first_names) + ' ' + random.choice(last_names)

        # generate a random age
        age = random.randint(18, 80)

        # generate a random phone number
        phone_number = '555-' + str(random.randint(100, 999)) + '-' + str(random.randint(1000, 9999))

        # generate a random email address
        email = name.lower().replace(' ', '.') + '@gmail.com'

        # randomly select a location from the predefined list
        selected_location = random.choice(locations)

        # extract location details
        address = {
            "country": "United States",  # You can customize this based on your needs
            "city": selected_location["city"],
            "state": selected_location["state"]
        }

        # append generated data to the list
        fake_data.append({
            "name": name,
            "age": age,
            "phone_number": phone_number,
            "email": email,
            "address": address
        })

    return fake_data

# example usage:
fake_entries = generate_realistic_addresses(num_entries_to_generate)
for entry in fake_entries:
    print('name:', entry["name"])
    print('age:', entry["age"])
    print('phone_number:', entry["phone_number"])
    print('email:', entry["email"])
    print('address:', entry["address"])
    print('\n')

