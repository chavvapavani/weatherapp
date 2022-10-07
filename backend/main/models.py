from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=60,blank=False)
    weather_condition = models.CharField(max_length=500)
    temperature=models.FloatField()
    humidity=models.FloatField()
    pressure=models.FloatField()
    minimum_temp=models.FloatField()
    maximum_temp=models.FloatField()
    icon=models.CharField(max_length=60)
    cod=models.CharField(max_length=60)

    def __str__(self):
        return self.city

