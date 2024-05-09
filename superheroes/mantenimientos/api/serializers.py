# Importamos desde rest_framework serializers
from rest_framework import serializers
from mantenimientos.models  import Personaje

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'