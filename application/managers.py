from django.db import models

#Definicio de manager para actualizacion
class ClimaManager(models.Manager):

    def actualizar_clima(self,values):
        return self.update(
            temp=values["temp"],
            wind_speed=values["wind_speed"],
            wind_direction=values["wind_direction"],
            longitud=values["longitud"],
            latitud=values["latitud"],
            name= values["name"]
        )
