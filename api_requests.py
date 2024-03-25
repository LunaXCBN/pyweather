import json
import requests
import global_vars
import functions
import spinners

import time

def get_lon_lat():
    user_country, user_city = functions.get_user_location()
    print('\n')
    spinners.wspinner(True, "Converting to lat/lon...")
    link = global_vars.geocode.format(user_country, user_city)
    response = requests.get(link, headers=global_vars.headers)

    # Get longitude and latitude from Geocode API
    lonlat_data = json.loads(response.text)
    lat = lonlat_data[0]['lat']
    lon = lonlat_data[0]['lon']

    lonlat_ready = True
    if lonlat_ready == True:
        spinners.wspinner(False)
    return user_country, user_city, lat, lon

def get_weather(lat, lon):
    openmeteo_link = global_vars.openmeteo.format(lat, lon)
    print(openmeteo_link)
    spinners.wspinner(True, "Getting weather data...")
    response = requests.get(openmeteo_link, headers=global_vars.headers)

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

    data_ready = True
    if data_ready == True:
        spinners.wspinner(False)
    # Print data in a human readable format
    return data_ready, temp, temp_units, humidity, humidity_units, wind, wind_units