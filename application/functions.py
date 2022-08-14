import requests, os, json
from .models import Clima, Log

#obtener url y Key
URL = os.environ['URL']
KEY = os.environ['KEY']

#Funcion para llamar a la API de climas
def CallApi(id_city):
    request = requests.get(URL, params={"city_id": id_city, "key":KEY})
    response_json = json.loads(request.text)
    #Verificar si el codigo es 200
    if (request.status_code != 200):
        #Crear registro en logs de fallo
        Log.objects.create(
            msg = "Error al llamar el api. Status:" + str(request.status_code)
        )
        #Devolver falso en caso que fallo
        return False

    #Ingresar al atributo data
    response_json = response_json["data"]
    for res in response_json:
        default_values = {
                'temp':res["temp"],
                'wind_speed':res["wind_spd"],
                'wind_direction':res["wind_cdir_full"],
                'longitud':res["lon"],
                'latitud':res["lat"],
                'name':res["city_name"]
            }
        #devolver el primer registro, esto debito a que la API devuelve varios registros en el json y no uno
        return default_values
