from .constants import APP_ID
import requests


def read_weather_map_api(city):

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={APP_ID}"
    api_data = requests.get(weather_url).json()

    return api_data
