import json
import requests
import global_vars

def get_lon_lat(link):
    ## Not removed for debugging reasons
    #print(link)
    response = requests.get(link, headers=global_vars.headers)
    ## Not removed for debugging reasons
    #print("Geocode response:", response)

    # Get longitude and latitude from Geocode API
    lonlat_data = json.loads(response.text)
    global_vars.lon = lonlat_data[0]['lon']
    global_vars.lat = lonlat_data[0]['lat']
    # Print values for confirmation
    print("Longitude:", global_vars.lon)
    print("Latitude:", global_vars.lat)

def get_weather(lat, lon):
    openmeteo_link = global_vars.openmeteo.format(lat, lon)
    ## Not removed for debugging reasons
    #print(openmeteo_link)
    response = requests.get(openmeteo_link, headers=global_vars.headers)
    ## Not removed for debugging reasons
    #print("Openmeteo response:", response)

    # Get weather data from Openmeteo API
    weather_data = json.loads(response.text)
    # Set unit variables
    temp_units = weather_data['current_units']['temperature_2m']
    humidity_units = weather_data['current_units']['relative_humidity_2m']
    wind_units = weather_data['current_units']['wind_speed_10m']

    # Set weather variables
    temp = weather_data['current']['temperature_2m']
    humidity = weather_data['current']['relative_humidity_2m']
    wind = weather_data['current']['wind_speed_10m']

    # Print data in a human readable format
    print(f"Temperature: {temp}{temp_units}")
    print(f"Relative humidity: {humidity}{humidity_units}")
    print(f"Wind speed: {wind}{wind_units}")