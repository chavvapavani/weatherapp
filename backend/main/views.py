from rest_framework.response import Response
import requests
from rest_framework.views import APIView
class Api(APIView):  
    def get(self,request,format=None): 
        city=request.data.get('city') #getting the city name as input by the user
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
        data=requests.get(url)   #requesting the given url for the data
        json_data=data.json()  #converting the data into json format
        #getting only required fields from json data
        response_data = {
            "weather_condition": json_data['weather'][0]['description'],
            "icon": json_data['weather'][0]['icon'],
            "temperature": json_data['main']['temp'],
            "city": json_data['name'],
            "humidity":json_data['main']['humidity'],
            "pressure":json_data['main']['pressure']
        }
        return Response(response_data)
       


