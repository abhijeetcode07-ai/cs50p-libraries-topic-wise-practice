# Question 8
# Write a program that:
# 1. Takes city name from command line argument using sys.argv
# 2. Uses requests module to fetch weather data from OpenWeatherMap API
# 3. Converts the response into JSON using response.json()
# 4. Iterates over the "main" dictionary using a for loop
# 5. Prints ALL weather details like temperature, humidity, pressure, etc.
# 6. Temperature should be in Celsius (use units=metric)
# 7. Show an error using sys.exit() if city name is not provided


import sys
import requests


YOUR_API_KEY = "0c3178d52a7f09c510438285ee5ba3ac"
if len(sys.argv) < 2 :
    sys.exit("TOO FEW ARGUMENTS")

elif len(sys.argv) > 2 :
    sys.exit("TOO MANY ARGUMENTS")     
     
city  = sys.argv[1] 
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR_API_KEY}&units=metric")


data = response.json()

for key in data["main"] :
    print(key,data["main"][key], sep = " -- ")