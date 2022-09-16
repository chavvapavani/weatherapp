
from unittest.util import _MAX_LENGTH
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework import serializers
class WeatherAPiSerializer(serializers.Serializer):
    city=serializers.CharField(max_length=60)
class WeatherApi(APIView):
    serializer_class=WeatherAPiSerializer
    def post(self,request): 
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        city=serializer.validated_data.get('city') #getting the city name as input by the user
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
        data=requests.get(url)   #requesting the given url for the data
        json_data=data.json()  #converting the data into json form
        #getting only required fields from json data
        response_data = {
            "weather_condition": json_data['weather'][0]['description'],
            "temperature": json_data['main']['temp'],
            "city": json_data['name'],
            "humidity":json_data['main']['humidity'],
            "pressure":json_data['main']['pressure'],
            "minimum_temp":json_data['main']['temp_min'],
            "maximum_temp":json_data['main']['temp_max'],
            "icon":json_data['weather'][0]['icon'],

        }
        return Response(response_data)
class WeatherForecast(APIView):
    serializer_class=WeatherAPiSerializer
    def post(self,request): 
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        city=serializer.validated_data.get('city')
        url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
        data=requests.get(url)   
        json_data=data.json()
        date_list=[]
        forecast_data={}
        for i in range(0,json_data['cnt']):
                date=json_data['list'][i]['dt_txt'].split(" ")[0]
                if date not in date_list:
                    date_list.append(date)
                    each_date={}
                    each_date.update({"temperature":json_data['list'][i]['main']['temp']})
                    each_date.update({"descriptrion":json_data['list'][i]['weather'][0]['description']})
                    each_date.update({"icon":json_data['list'][i]['weather'][0]['icon']})
                    each_date.update({"date":date})
                    forecast_data.update({date:each_date})
        return Response(forecast_data)




    