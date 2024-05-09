from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mantenimientos.api.serializers import PersonajeSerializer
from mantenimientos.models import Personaje
from django.db import IntegrityError

# Definimos nuestra vista de API para el modelo Personaje
class PersonajeAPIView(APIView):
    # Método separado para crear un nuevo personaje
    def create_personaje(self, data):
        serializer = PersonajeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise ValueError(serializer.errors)

    # Definimos el método POST para crear un nuevo personaje
    def post(self, request):
        # Usamos un bloque try/except para manejar posibles errores
        try:
            # Intentamos crear un nuevo personaje...
            personaje_data = self.create_personaje(request.data)
            # Si se crea con éxito, devolvemos una respuesta con un mensaje de éxito
            return Response(
                {'mensaje': 'Personaje creado correctamente', 'data': personaje_data}, status=status.HTTP_201_CREATED
                )
        except ValueError as e:
            # Si los datos no son válidos, devolvemos una respuesta con los errores del serializador
            return Response({'mensaje': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            # Si se produce un error de integridad (por ejemplo, un nombre de personaje duplicado),
            # devolvemos una respuesta con un mensaje de error específico
            return Response({'mensaje': 'El personaje ya existe'}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            # Para cualquier otro error, devolvemos una respuesta con el mensaje de error
            return Response({'mensaje': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            # Obtenemos la lista de personajes activos
            #personaje_lista = Personaje.objects.filter(is_active = True)
            
            # Obtenemos la lista de todos los personajes
            personaje_lista = Personaje.objects.all()
            
            # Creamos un serializador para convertir los datos del modelo a formato JSON
            serializer = PersonajeSerializer(personaje_lista, many=True)
            
            # Devolvemos una respuesta con los datos de los personajes
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Para cualquier otro error, devolvemos una respuesta con el mensaje de error
            return Response({'mensaje': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self, request, pk=None):
        try:
            # Obtenemos el personaje que queremos actualizar
            personaje = Personaje.objects.get(pk=pk)
            
            # Creamos un serializador con los datos de la petición
            serializer = PersonajeSerializer(personaje, data=request.data, partial=True)
            
            # Si los datos son válidos, guardamos el personaje actualizado
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Personaje.DoesNotExist:
            return Response({'mensaje': 'El personaje no existe'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'mensaje': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        try:
            # Obtenemos el personaje que queremos eliminar
            personaje = Personaje.objects.get(pk=pk)
            
            # Eliminamos el personaje
            personaje.delete()
            
            # Devolvemos una respuesta indicando que la eliminación fue exitosa
            return Response({'mensaje': 'Personaje eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Personaje.DoesNotExist:
            return Response({'mensaje': 'El personaje no existe'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'mensaje': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


