import beaupy
import json
import time
import functions
import os
import maps
from subprocess import call

# Function for first time launch configuration.
def configuration():
    with open('config.json', 'r') as f:
        config = json.load(f)

    if config['first_launch'] == True:
        banner_text = "First time configuration."
    else:
        banner_text = "Configuration."
    
    # Call figlet banner function from functions.py
    functions.pyweather_banner(banner_text)

    # User input for either Celsius or Fahrenheit using Beaupy
    print("Please select your preferred temperature unit.")
    temp = beaupy.select(options = ["Celsius (°C)", "Fahrenheit (°F)"],
                                cursor=">",
                                cursor_style="purple")
    
    # Change values in config.json according to user input.
    if temp == "Celsius (°C)":
        config["units"]["temp_unit"] = "celsius"
    else:
        config["units"]["temp_unit"] = "fahrenheit"

    # Call figlet banner function from functions.py
    functions.pyweather_banner(banner_text)

    # User input for either Metric or Imperial speed units.
    print("Please select your preferred speed unit.")
    speed = beaupy.select(options = ["Metric (km/h)", "Imperial (mph)"],
                          cursor=">",
                          cursor_style="purple")
    
    # Change values in config.json according to user input.
    if speed == "Metric (km/h)":
        config["units"]["speed_unit"] = "metric"
    else:
        config["units"]["speed_unit"] = "imperial"
    
    # Call figlet banner function from functions.py
    functions.pyweather_banner(banner_text)

    # User input for preferred weather variables.
    print("Please select your preferred weather variables.")
    weather_vars = beaupy.select_multiple(options = ["Temperature",
                                                     "Relative Humidity",
                                                     "Apparent Temperature",
                                                     "Is Day or Night",
                                                     "Rain",
                                                     "Showers",
                                                     "Snowfall",
                                                     "Cloud cover Total",
                                                     "Wind Speed",
                                                     "Wind Direction",
                                                     "Wind Gusts"])
    # Loop through weather_vars map for weather variables
    for i in maps.weather_vars:
        # Check if variables match with selections
        if i in weather_vars:
            # Set variable to True in config.json
            w = maps.weather_vars.get(i)
            config["variables"][w] = True
        # If variable does not match with selections
        else:
            # Set variable to False in config.json
            w = maps.weather_vars.get(i)
            config["variables"][w] = False

    # Call figlet banner function from functions.py
    functions.pyweather_banner(banner_text)

    # Finish first launch configuration up.
    # Set first_launch to false to indicate that initial setup has been done.
    config["first_launch"] = False

    # Write changes to config.json
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    print("Configuration done! Exiting to dashboard in 1...")
    time.sleep(1)
    dashboard()

def dashboard():
    # Call figlet banner function from functions.py
    functions.pyweather_banner("Python weather application made by LunaXCBN")

    dashboard = beaupy.select(options = ["Weather", "Config", "Quit"],
                              cursor=">",
                              cursor_style="purple")
    
    if dashboard == "Weather":
        pass
    if dashboard == "Config":
        configuration()
    if dashboard == "Quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()
