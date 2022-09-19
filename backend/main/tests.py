from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class WeatherTest(APITestCase):
    def test_valid_city_name(self):
        url = 'http://127.0.0.1:8000/' 
        response = self.client.post(url, {'city':'chennai'})  
        self.assertEquals(response.json()["cod"],"200")
    def test_empty_city_name(self):
        url = 'http://127.0.0.1:8000/' 
        response = self.client.post(url, {'city':' '})  
        self.assertEquals(response.json()["cod"],"404")
    def test_city_name_including_special_character(self):
        url = 'http://127.0.0.1:8000/' 
        response = self.client.post(url, {'city':'chenn@i'})  
        self.assertEquals(response.json()["cod"],"404")
    def test_city_name_with_numbers(self):
        url = 'http://127.0.0.1:8000/' 
        response = self.client.post(url, {'city':'123'})  
        self.assertEquals(response.json()["cod"],"405")
    
    def test_valid_city_forecast(self):
        url = 'http://127.0.0.1:8000/forecast/' 
        response = self.client.post(url, {'city':'chennai'})  
        self.assertEquals(response.json()[-1]["cod"],200)

    def test_empty_city_forecast(self):
        url = 'http://127.0.0.1:8000/forecast/' 
        response = self.client.post(url, {'city':' '})  
        self.assertEquals(response.json()["cod"],400)
    def test_city_name_including_numbers_forecast(self):
        url = 'http://127.0.0.1:8000/forecast/' 
        response = self.client.post(url, {'city':'ch123'})  
        self.assertEquals(response.json()["cod"],400)
    def test_city_name_including_special_characters_forecast(self):
        url = 'http://127.0.0.1:8000/forecast/' 
        response = self.client.post(url, {'city':'chenn@i'})  
        self.assertEquals(response.json()["cod"],400)


