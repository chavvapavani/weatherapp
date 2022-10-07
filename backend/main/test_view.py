from django.urls import reverse
from rest_framework.test import APITestCase

#testcases for currentweather api
class WeatherTest(APITestCase):

    def test_valid_city_name(self):
        url=reverse('currentweather')
        response=self.client.post(url,data={"city" : "chennai" })
        self.assertEquals(response.data['cod'],'200')

    def test_empty_city(self):
         url=reverse('currentweather')
         response=self.client.post(url,data={"city" : "" })
         self.assertEquals(response.data['cod'],'404')

    def test_city_with_numbers(self):
         url=reverse('currentweather')
         response=self.client.post(url,data={"city" : 1212 })
         self.assertEquals(response.data['cod'],'405')

    def test_city_with_specialcharacters(self):
         url=reverse('currentweather')
         response=self.client.post(url,data={"city" : "chenn@i" })
         self.assertEquals(response.data['cod'],'404')

#testcases for forecast weather api
class ForecastTest(APITestCase):

    def test_valid_city_name(self):
        url=reverse('forecastweather')
        response=self.client.post(url,data={"city" : "chennai" })
        self.assertEquals(response.data[-1]['cod'],200)

    def test_empty_city(self):
         url=reverse('forecastweather')
         response=self.client.post(url,data={"city" : "" })
         self.assertEquals(response.data['cod'],400)

    def test_city_with_numbers(self):
         url=reverse('forecastweather')
         response=self.client.post(url,data={"city" : 1212 })
         self.assertEquals(response.data['cod'],405)

    def test_city_with_specialcharacters(self):
         url=reverse('forecastweather')
         response=self.client.post(url,data={"city" : "chenn@i" })
         self.assertEquals(response.data['cod'],400)

