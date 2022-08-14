from application.models import Clima

#arreglo de ciudades elegidas
ID_CITIES = [
    3871336,
    2657896,
    2193733,
    2147714,
    2643743,
    4064006
]

#funcion para crear u obtener las ciudades, las crea si no estan, las obtiene si ya existen
def CreateCities(city):
        Clima.objects.get_or_create(
            id_clima=city
        )

#funcion para recorrer todas las ciudades
def CreateCitiesOnceTime():
    for city in ID_CITIES:
        CreateCities(city)
    

