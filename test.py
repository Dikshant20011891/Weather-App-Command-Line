# import requests
# import json
# import argparse

# def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=cbf04a5926dc62ad1fd20d61fa66b75e&units=metric"
#     response = requests.get(url)
#     data = json.loads(response.text)

#     # print(json.dumps(data, indent=4))
    
#     if data["cod"] == "404":
#         print("City not found.")
#     else:
#         temperature = data["main"]["temp"]
#         weather_description = data["weather"][0]["description"]
#         print(f"Weather in {city}: {weather_description}")
#         print(f"Temperature: {temperature}°C")

# def main():
#     parser = argparse.ArgumentParser(description="Take the city name input")
#     parser.add_argument("city")

#     args = parser.parse_args()
#     city = args.city

#     get_weather(city)

# if __name__ == "__main__":
#     main()

import requests
import json
import argparse

# Dictionary to store cached weather data
weather_cache = {}

def get_weather(city):
    # Check if weather data is already in cache
    if city in weather_cache:
        print("Retrieving weather data from cache...")
        temperature, weather_description = weather_cache[city]
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=cbf04a5926dc62ad1fd20d61fa66b75e&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)

        if data["cod"] == "404":
            print("City not found.")
            return

        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

        # Store weather data in cache
        weather_cache[city] = (temperature, weather_description)

    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature}°C")

def main():
    parser = argparse.ArgumentParser(description="Take the city name input")
    parser.add_argument("city")

    args = parser.parse_args()
    city = args.city

    get_weather(city)

if __name__ == "__main__":
     main()