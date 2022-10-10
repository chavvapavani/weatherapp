from asyncio.windows_events import NULL
import sys
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from .models import Weather
from .serializers import WeatherAPiSerializer, WeatherLens, OutputDataSerializer, WeatherSerializer


class WeatherApi(APIView):

    input_serializer=WeatherAPiSerializer
    output_serializer=OutputDataSerializer
    app_id = "b0b2a8c6eb68cf455d2b353ed0537b55"

    def post(self,request):

        # try:
        #     import ipdb
        #     ipdb.set_trace()

            serializer=self.input_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            city=serializer.validated_data.get("city")
            if(city.isnumeric()):
                return Response({"cod":"405"})

            weather_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={self.app_id}"
            api_data=requests.get(weather_url).json()
            if api_data['cod'] == '404':
                return Response({'error':api_data['message']})

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
            
            db_weather = Weather.objects.filter(city= data['city'])
            #db_weather.update(weather_condition = data['weather_condition'] )
            if len(db_weather) < 1:
                Weather(**data)
            obj=WeatherLens(data)
            data_serializer=self.output_serializer(obj)
            return Response(data_serializer.data)
        
        # except:
            
        #     return Response({"cod":"404"})


class WeatherForecast(APIView): #forecastApi
    serializer_class=WeatherAPiSerializer
    def post(self,request):
        try: 
            serializer=self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            city=serializer.validated_data.get('city')#getting the city name as input by the user
            if(city.isnumeric()):   #checking whether the city name contains numbers or not
                return Response({"cod":405})
            forecasturl=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
            data=requests.get(forecasturl) #requesting the given url for the data
            json_data=data.json()#converting the data into json form
            date_list=[]
            forecast_data=[]#list to store output data
            for i in range(0,json_data['cnt']):
                date=json_data['list'][i]['dt_txt'].split(" ")[0]#getting date from the json_data
                if date not in date_list:
                    date_list.append(date)
                    each_date={}
                    each_date.update({"temperature":json_data['list'][i]['main']['temp']})
                    each_date.update({"description":json_data['list'][i]['weather'][0]['description']})
                    each_date.update({"icon":json_data['list'][i]['weather'][0]['icon']})
                    each_date.update({"date":date})               
                    forecast_data.append(each_date)
            forecast_data.append({"cod":200})            
            return Response(forecast_data)
        except:
            return Response({"cod":400})




    