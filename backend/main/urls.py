
from django.urls import path
from . import views

urlpatterns = [
    path('',views.WeatherApi.as_view()),
    path('forecast/',views.WeatherForecast.as_view())
    
]

