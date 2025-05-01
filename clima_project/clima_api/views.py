from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClimaSerializer
from django.http import HttpResponse


API_KEY = '8cdeb77776a235824f142bb4807bb342'

class ClimaView(APIView):
    def get(self, request):
        ciudad = request.query_params.get('ciudad')
        if not ciudad:
            return Response({'error': 'Debes proporcionar una ciudad'}, status=status.HTTP_400_BAD_REQUEST)

        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ciudad}"
        respuesta = requests.get(url)
        datos = respuesta.json()

        if 'current' not in datos:
            return Response({'error': 'Error al obtener datos del clima'}, status=status.HTTP_502_BAD_GATEWAY)

        clima = {
            'ciudad': datos.get('location', {}).get('name'),
            'temperatura': datos.get('current', {}).get('temperature'),
            'descripcion': datos.get('current', {}).get('weather_descriptions', [])[0],
            'humedad': datos.get('current', {}).get('humidity'),
        }

        serializer = ClimaSerializer(data=clima)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def home(request):
    return HttpResponse("¡Bienvenido a la página de inicio!")
