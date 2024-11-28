"""
Create a command-line Weather App that fetches and displays current weather
information for a specified city using a weather API.

Requirements:
 - input temp_unit and city
 - fetch weather of required city
 - check for errors
 - display weather details

# Remember first install requests using "python -m pip install requests"
by pasting this in terminal. Otherwise you'll face err

"""

import requests


URL_KEY = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "6ac8d21c84b9caf7b3c2d560113efe27"

def fetch_weather(city_name, unit):
    try:
        # Define the unit system: Celsius, Fahrenheit, or Kelvin
        units = {"celsius": "metric", "fahrenheit": "imperial", "kelvin": "standard"}

        # ensure valid unit input
        if unit.lower() not in units:
            print("Invalid unit. Defaulting to Celsius.")
            unit = "celsius"

        # make an API request
        response = requests.get(URL_KEY, params={
            "q" : city_name,
            "appid" : API_KEY,
            "units" : unit.lower()
        })
        data = response.json()

        # check for valid response
        if response.status_code == 200:
            return data
        elif response.status_code == 404:
            return {"error" : "City not found."}
        else:
            return {"error" : "Something went wrong, Please try again"}

    except requests.exceptions.RequestException as e:
        return {"error" : f"Network error: {e} "}

def display_weather(data, unit):
    if "error" in data:
        print(data["error"])
    else:
        # get temperature and weather description
        city = data.get("name")
        temp = data["main"].get("temp")
        humidity = data["main"].get("humidity")
        wind_speed = data["wind"]["speed"]
        feels_like_temp = data["main"]["feels_like"]
        description = data["weather"][0].get("description")

        # display details
        print(f"\nWeather in {city}: ")
        # Format temperature based on the unit chosen
        if unit == "celsius":
            temp_unit = "°C"
        elif unit == "fahrenheit":
            temp_unit = "°F"
        else:
            temp_unit = "K"
        print(f"Temperature:       {temp}{temp_unit}")
        print(f"Humidity:          {humidity}")
        print(f"Wind speed:        {wind_speed}")
        print(f"Description:       {description}")
        print(f"Feels like temp:   {feels_like_temp}{temp_unit}")

def main():
    print("Welcome to The Weather App")
    print("You can check the weather in Celsius, Fahrenheit, or Kelvin.")
    # Ask the user for the temperature unit (Celsius, Fahrenheit, Kelvin)
    unit = input("\nEnter the unit (celsius, fahrenheit, kelvin): ").strip().lower()

    while True:
        # ask for city name
        city_name = input("Enter the name of city:").strip()

        # fetch and display data
        weather_data = fetch_weather(city_name, unit)
        display_weather(weather_data, unit)

        # seperator for readability
        print("\n" + "_" * 30)

        # ask for other city
        choice = input("Do you want to check for another city? (yes/no) ")
        if choice.lower() == "no":
            print("Thank you for using the Weather App. Good Bye!")
            break

main()
