
from rest_framework import serializers

class ClimaSerializer(serializers.Serializer):
    ciudad = serializers.CharField()
    temperatura = serializers.FloatField()
    descripcion = serializers.CharField()
    humedad = serializers.IntegerField()