# API links
openmeteo = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m&hourly=temperature_2m"
geocode = "https://geocode.maps.co/search?q={}+{}"

# Variable defaults
user_country = ""
user_city = ""

# Header defaults
headers = {'content-type': 'application/json'}