"""
geocode_lookup.py - A script to perform geocoding using the Google Maps Geocoding API.

This script takes user input for a location, sends a request to the Google Maps Geocoding API,
and retrieves and displays the latitude, longitude, and formatted address of the specified location.

Please note that an API key is required for making requests to the Google Maps Geocoding API.

Usage:
    python geocode_lookup.py
"""

import json
import urllib.request, urllib.error, urllib.parse

def perform_geocoding(address):
    """
    Performs geocoding using the Google Maps Geocoding API for the specified address.

    Parameters:
        address (str): The location to be geocoded.

    Returns:
        None
    """
    # Google Maps Geocoding API URL
    serviceurl = "https://maps.google.com/maps/api/geocode/json?"

    # Construct the API request URL
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)

    # Send the request to the Google Maps Geocoding API
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError as e:
        js = None
        print(f"Error decoding JSON: {e}")
        return

    if not js or 'status' not in js or js['status'] != 'OK':
        print("=== Failure to retrieve ===")
        print(data)
        return

    # Display the formatted JSON response
    print(json.dumps(js, indent=4))

    # Extract and display the latitude, longitude, and formatted address
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("Latitude:", lat, "Longitude:", lng)

    location = js["results"][0]["formatted_address"]
    print("Formatted Address:", location)

if __name__ == "__main__":
    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        perform_geocoding(address)
