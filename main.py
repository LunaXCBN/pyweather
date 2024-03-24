import global_vars
import api_requests
import json
import time
import functions
import interface
import os

# Check if file exists and if first_launch is set to True
file_found = os.path.isfile('./config.json')
if file_found == True:
    # If file is found, open the file for reading.
    with open('config.json', 'r') as f:
        config = json.load(f)
    # Check if first_launch is set to True.
    ## If set to true, go to first launch config
    if config['first_launch'] == True:
        interface.configuration()
    # If set to false, go to dashboard
    else:
        interface.dashboard()
# If file is not found, go to first launch config
else:
    functions.create_jsonfile("config")
    interface.configuration()   

# Call geocode API to translate User Input to Longitude and Latitude
# This also calls get_user_location() in functions.py
lonlat = api_requests.get_lon_lat()

# Call openmeteo to get weather data
weather = api_requests.get_weather(global_vars.lat, global_vars.lon)

# Clear console
if weather[0] and lonlat[2] == True:
    functions.pyweather_banner("Done!")

# Print user location
print(f"Country: {lonlat[0]}")
print(f"City: {lonlat[1]}\n")

# Print longitude and latitude
print(f"Lon: {global_vars.lon}")
print(f"Lat: {global_vars.lat}")

# Combine data and units
temp = f"{weather[1]}{weather[2]}"
humidity = f"{weather[3]}{weather[4]}"
wind = f"{weather[5]} {weather[6]}"

# Print weather data
print(f"Temperature: {temp}")
print(f"Relative humidity: {humidity}")
print(f"Wind speed: {wind}")

input("\nPress any key to continue...")
interface.dashboard()
