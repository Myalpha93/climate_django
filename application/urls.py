from django.urls import path

#Buena practica de solo trare lo necesario
from .views import UpdateDataClimas, ApiClimaRetriewView
from rest_framework_swagger.views import get_swagger_view

app_name = "clima_apps"

urlpatterns = [
    path(
        'api/climas/',
        UpdateDataClimas.as_view(),
        name='actualizar-climas'
    ),
    path(
        'api/climas/<pk>',
        ApiClimaRetriewView.as_view(),
        name='obtener-clima'
    ),
]