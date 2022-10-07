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
        serializer=self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city=serializer.validated_data.get("city")
        weather_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={self.app_id}"
        data=requests.get(weather_url).json()

        if(city.isnumeric()):
            return Response({"cod":"405"})

        data = {
            "weather_condition": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "city": data["name"],
            "humidity":data["main"]["humidity"],
            "pressure":data["main"]["pressure"],
            "minimum_temp":data["main"]["temp_min"],
            "maximum_temp":data["main"]["temp_max"],
            "icon":data["weather"][0]["icon"],
            "cod":"200",
        }
        #weathervar = Weather.objects.create(**data['data'])
        db_weather = Weather.objects.filter(city=city, cod="200")
        if len(db_weather) < 0:
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




    