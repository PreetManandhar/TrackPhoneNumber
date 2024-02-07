
#import libraries
#pip install phonenumbers
#pip install folium

import phonenumbers
from phonenumbers import geocoder
import folium
from test import number


#to know location of number
check_number = phonenumbers.parse(number)
#using geocode for location in english
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


#to know mobile carriers
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))



