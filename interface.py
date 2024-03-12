import click
import json

def first_launch_config():
    

with open('config.json', 'r') as f:
    config = json.load(f)

if config['first_launch'] == True:
    print("True")
    first_launch_config()
else:
    print("False")
