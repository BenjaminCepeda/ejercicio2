from django.db import models


class Dato(models.Model):
    queryDate = models.DateTimeField(auto_now=True,verbose_name='QueryDate')
    temperature = models.FloatField(null=False,verbose_name='Temperature')
    humidity = models.IntegerField(null=False,verbose_name='Humidity')



