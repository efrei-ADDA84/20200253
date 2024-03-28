import os

import requests


def get_weather(latitude, longitude):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = float(input("Latitude : "))
    longitude = float(input("Longitude : "))
    weather_data = get_weather(latitude, longitude)
    print(weather_data)
