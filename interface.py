import beaupy
import json
import time
import functions
import os
from subprocess import call

# Open config.json in read-only mode
with open('config.json', 'r') as f:
    config = json.load(f)

# Function for first time launch configuration.
def first_launch_config():
    # Call figlet banner function from functions.py
    functions.pyweather_banner("First time configuration.")

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
    functions.pyweather_banner("First time configuration.")

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
    functions.pyweather_banner("First time configuration.")

    # Finish first launch configuration up.
    # Set first_launch to false to indicate that initial setup has been done.
    config["first_launch"] = False

    # Write changes to config.json
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    print("First launch configuration done!")
    time.sleep(1)
    dashboard()

# Function for first time launch configuration.
def configuration():
    # Call figlet banner function from functions.py
    functions.pyweather_banner("Config.")

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
    functions.pyweather_banner("Config.")

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
    functions.pyweather_banner("Configuration done!")

    # Write changes to config.json
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    print("Unit for temperature:", config["units"]["temp_unit"])
    print("Unit for speed:", config["units"]["speed_unit"], "\n")
    input("Press any key to continue...")
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