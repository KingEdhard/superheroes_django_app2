from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
# Desarrollo del modelo

class Personaje(models.Model):
    # Configurar los atributos del modelo
    id = models.AutoField(primary_key=True, editable=False)
    
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1), MaxLengthValidator(50)], unique=True)
    
    description = models.TextField(validators=[MinLengthValidator(1)])
    
    CATEGORIES = [
        ('SuperHéroe', 'SuperHéroe'),
        ('Villano', 'Villano')
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORIES, default='SuperHéroe')
    
    ABILITIES = [
        ('Fuerza', 'Fuerza'),
        ('Velocidad', 'Velocidad'),
        ('Inteligencia', 'Inteligencia'),
        ('Telepatía', 'Telepatía'),
        ('Invisibilidad', 'Invisibilidad'),
        ('Vuelo', 'Vuelo'),
        ('Teletransportación', 'Teletransportación'),
        ('Manipulación del tiempo', 'Manipulación del tiempo'),
        ('Regeneración', 'Regeneración'),
        ('Manipulación de la energía', 'Manipulación de la energía'),
    ]
    
    ability = models.CharField(max_length=50, choices=ABILITIES, default='Fuerza')
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name.strip().capitalize()
