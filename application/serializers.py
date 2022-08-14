from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Clima

class ClimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clima
        fields = ("__all__")