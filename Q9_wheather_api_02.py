# Question 9
# Write a Python program that:
# 1. Takes a city name from the command line (sys.argv)
# 2. Fetches weather data from OpenWeatherMap API
# 3. Extracts and prints ONLY the weather description 
#    (like "clear sky", "haze", "rain", etc.)
# Hint: The "weather" key in the JSON response is a LIST of dictionaries.
# Example output: Weather description: clear sky
#
# Make sure to handle the case when city name is missing with sys.exit()


import requests
import sys


API_ID = "0c3178d52a7f09c510438285ee5ba3ac"

if len(sys.argv) < 2 :
    sys.exit("TOO FEW ARGUMENTS")

elif len(sys.argv) > 2 :
    sys.exit("TOO MANY ARGUMENTS")

CITY = sys.argv[1]

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_ID}&units=metric")

data = response.json()

for key in data["weather"][0] :
    if key == "id" :
        continue
    print(key, data["weather"][0][key], sep = " -- ")

