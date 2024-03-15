import os
from pyfiglet import Figlet

fig = Figlet(font='cybermedium')

def get_user_location():
    # Take users country
    user_country = input("Target country: ")
    # Take users city
    user_city = input("Target city: ")

    return user_country, user_city

def pyweather_banner(text: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fig.renderText("pyweather"), f"{text}\n")
