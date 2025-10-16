### VERY SHORT EXAMPLE SCRIPT

from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent="jupyter")
city_country = "BURJ KHALIFA, United Arab Emirates"
location = geolocator.geocode(city_country)
devnet_lat = location.latitude
devnet_lon = location.longitude
coordinates = [devnet_lat, devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap', zoom_start=24)
map.save("map.html")
print("map.html")