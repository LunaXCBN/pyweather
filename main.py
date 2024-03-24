import json
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
