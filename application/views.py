import random

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
# Create your views here.
from .models import Clima
from .serializers import ClimaSerializer

from .functions import CallApi

class UpdateDataClimas(APIView):

    def post(self, request,*args,**kwargs):
        #Obtener numero random de 1 a 10
        random_number = random.randint(1, 10)
        #verificar si el numero es menor a 2
        if (random_number <=2):
            #Respuesta en caso de que sea menor a 2
            return Response(
                    {
                        "msg":"The API Request Failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        #Obtener todas las ciduades
        cities = Clima.objects.all()
        print("ciudades")
        print(cities)
        #recorrer todas las ciudades
        for city in cities:
            #Obtener valores de la API de la ciudad, llamada a funcion
            values = CallApi(city.id_clima)
            #Verificar si fue correcta la respuesta
            if values == False:
                #Devolver que hubo un error al actualizar
                return Response(
                    {
                        "msg":"Error al actualizar las ciudades"
                    },
                    status=status.HTTP_206_PARTIAL_CONTENT
                )
            #Actualizar las ciudades
            Clima.objects.actualizar_clima(values)
        
        return Response(
                    {
                        "msg":"Ciudades actualizadas correctamente"
                    },
                    status=status.HTTP_200_OK
                )

class ApiClimaRetriewView(RetrieveUpdateAPIView):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer
