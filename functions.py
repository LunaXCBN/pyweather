import os
import json
import time
from pyfiglet import Figlet

import api_requests
import global_vars
import interface

def get_user_location():
    # Take users country
    user_country = input("Target country: ")
    # Take users city
    user_city = input("Target city: ")

    return user_country, user_city

def pyweather_banner(text: str):
    fig = Figlet(font='cybermedium')

    os.system('cls' if os.name == 'nt' else 'clear')
    print(fig.renderText("pyweather"), f"{text}\n")

def create_jsonfile(name: str):
    # Declare data for config file to avoid error.
    data = {
            'first_launch': True,
            'units': {

                },
            'variables': {

                }
            }

    # Open json file for writing
    with open(name + ".json", 'w') as fp:
        json.dump(data, fp)

    # Check if file was created
    if os.path.isfile('./config.json'):
        pass
    else:
        print("Creating 'config.json' failed! Quitting in 2 seconds...")
        time.sleep(2)

def clear_and_quit():
    os.system("cls" if os.name == "nt" else "clear")
    quit()

def get_weather_main():
    # Call geocode API to translate User Input to Longitude and Latitude
    # This also calls get_user_location() in functions.py
    lonlat = api_requests.get_lon_lat()

    # Call openmeteo to get weather data
    weather = api_requests.get_weather(lonlat[2], lonlat[3])

    # Clear console
    if weather[0] and lonlat[2] == True:
        pyweather_banner("Done!")

    # Print user location
    print(f"Country: {lonlat[0]}")
    print(f"City: {lonlat[1]}\n")

    # Print longitude and latitude
    print(f"Lat: {lonlat[2]}")
    print(f"Lon: {lonlat[3]}")

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
