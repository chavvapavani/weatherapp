from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from .serializers import (
    WeatherAPiSerializer,
    OutputDataSerializer,
)
from .utils import get_values
from .view_models import read_weather_map_api


class WeatherApi(APIView):

    input_serializer = WeatherAPiSerializer
    output_serializer = OutputDataSerializer

    def post(self, request):

        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city = serializer.validated_data.get("city")
        if city.isnumeric():
            return Response({"cod": "405"})

        api_data = read_weather_map_api(city)
        if api_data["cod"] == "404":
            return Response({"error": api_data["message"]})

        obj = get_values(api_data)
        data_serializer = self.output_serializer(obj)
        return Response(data_serializer.data)


class WeatherForecast(APIView):  # forecastApi
    serializer_class = WeatherAPiSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            city = serializer.validated_data.get(
                "city"
            )  # getting the city name as input by the user
            if (
                city.isnumeric()
            ):  # checking whether the city name contains numbers or not
                return Response({"cod": 405})
            forecasturl = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
            data = requests.get(forecasturl)  # requesting the given url for the data
            json_data = data.json()  # converting the data into json form
            date_list = []
            forecast_data = []  # list to store output data
            for i in range(0, json_data["cnt"]):
                date = json_data["list"][i]["dt_txt"].split(" ")[
                    0
                ]  # getting date from the json_data
                if date not in date_list:
                    date_list.append(date)
                    each_date = {}
                    each_date.update(
                        {"temperature": json_data["list"][i]["main"]["temp"]}
                    )
                    each_date.update(
                        {
                            "description": json_data["list"][i]["weather"][0][
                                "description"
                            ]
                        }
                    )
                    each_date.update(
                        {"icon": json_data["list"][i]["weather"][0]["icon"]}
                    )
                    each_date.update({"date": date})
                    forecast_data.append(each_date)
            forecast_data.append({"cod": 200})
            return Response(forecast_data)
        except:
            return Response({"cod": 400})
