import global_vars
import api_requests
import interface

# Take users country
user_country = input("Target country: ")
print("Selected country: " + user_country + "\n")

# Take users city
user_city = input("Target city: ")
print("Selected city: " + user_city + "\n")

# Format Geocode API link to include user input
geocode_link = global_vars.geocode.format(user_city, user_country)
## Not removed for debugging reason
#print(geocode_link)

# Call geocode API to translate User Input to Longitude and Latitude
api_requests.get_lon_lat(geocode_link)

# Call openmeteo to get weather data
api_requests.get_weather(global_vars.lat, global_vars.lon)