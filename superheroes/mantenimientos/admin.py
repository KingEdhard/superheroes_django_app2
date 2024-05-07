from django.contrib import admin
from mantenimientos.models import Personaje
# Register your models here.

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ['name','category','ability'] 