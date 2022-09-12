from rest_framework.response import Response
import requests
from rest_framework.views import APIView
class Api(APIView):
    def get(self,request,format=None):
        url="http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=b0b2a8c6eb68cf455d2b353ed0537b55"
        data=requests.get(url)   #requesting the given url for the data
        json_data=data.json()  #converting the data into json format
        print(json_data)
        return Response(json_data) 


