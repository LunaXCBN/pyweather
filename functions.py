import os
import json
import time
from pyfiglet import Figlet

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

    data = {
            'first_launch': True,
            'units': {

                },
            'variables': {

                }
            }

    with open(name + ".json", 'w') as fp:
        json.dump(data, fp)

    if os.path.isfile('./config.json'):
        pass
    else:
        print("Creating 'config.json' failed! Quitting in 2 seconds...")
        time.sleep(2)
