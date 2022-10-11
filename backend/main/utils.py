from .models import Weather as weather_model
from .serializers import WeatherLens


def get_values(api_data: dict) -> dict:

    if api_data is not None:

        data = {
            "weather_condition": api_data["weather"][0]["description"],
            "temperature": api_data["main"]["temp"],
            "city": api_data["name"],
            "humidity":api_data["main"]["humidity"],
            "pressure":api_data["main"]["pressure"],
            "minimum_temp":api_data["main"]["temp_min"],
            "maximum_temp":api_data["main"]["temp_max"],
            "icon":api_data["weather"][0]["icon"],
            "cod":"200",
        }

        try:
            db_weather = weather_model.objects.get(city=data["city"])
            if db_weather:
                weather_model.objects.filter(city=data["city"]).update(
                    weather_condition=data["weather_condition"],
                    temperature=data["temperature"],
                    humidity=data["humidity"],
                    pressure=data["pressure"],
                    minimum_temp=data["minimum_temp"],
                    maximum_temp=data["maximum_temp"],
                    icon=data["icon"],
                )
        except Exception:
            weather_model.objects.create(**data)

        obj = WeatherLens(data)

        return obj
