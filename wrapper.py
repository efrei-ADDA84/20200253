import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
# print(os.environ.get('OPENWEATHER_API_KEY'))
def get_weather(latitude, longitude):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/weather')
def weather():
    latitude = float(request.args.get('lat'))
    longitude = float(request.args.get('lon'))
    weather_data = get_weather(latitude, longitude)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
