from rest_framework import serializers
from main.models import Weather

class WeatherLens(object):
    def __init__(self,weather_details):
        self.weather_details = weather_details


class WeatherAPiSerializer(serializers.Serializer):
    city=serializers.CharField(max_length=60,required=True)


class OutputDataSerializer(serializers.Serializer):
    weather_details = serializers.DictField(child = serializers.CharField())

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = (
            'city',
            'weather_condition',
            'temperature',
            'humidity',
            'pressure',
            'minimum_temp',
            'maximum_temp',
            'icon',
            'cod'

        )






