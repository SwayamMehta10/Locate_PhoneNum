import os
from dotenv import load_dotenv
load_dotenv()
number = os.getenv("NUMBER")
key = os.getenv("KEY")

import phonenumbers
import folium

# For country
from phonenumbers import geocoder
num = phonenumbers.parse(number)
country = geocoder.description_for_number(num, "en")
print(country)

# For service provider
from phonenumbers import carrier
service = phonenumbers.parse(number)
print(carrier.name_for_number(service, "en"))

# Getting latitude and longitude
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(country)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

# Showing location on map
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = country).add_to((myMap))

# Saving map as a HTML file
myMap.save("Location.html")