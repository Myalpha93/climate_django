from django.db import models
from .managers import ClimaManager
# Create your models here.


class Clima (models.Model):
    id_clima = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    temp = models.IntegerField(null=True, blank=True)
    wind_speed = models.IntegerField(null=True, blank=True)
    wind_direction = models.CharField(max_length=20,null=True, blank=True)
    longitud = models.DecimalField(null=True, blank=True,max_digits=10, decimal_places=2)
    latitud = models.DecimalField(null=True, blank=True,max_digits=10, decimal_places=2)

    objects = ClimaManager()

class Log (models.Model):
    id_log = models.IntegerField(primary_key=True)
    msg = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)