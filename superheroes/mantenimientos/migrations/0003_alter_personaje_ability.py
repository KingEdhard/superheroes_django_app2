# Generated by Django 5.0.4 on 2024-05-07 18:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0002_alter_personaje_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='ability',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Fuerza', 'Fuerza'), ('Velocidad', 'Velocidad'), ('Inteligencia', 'Inteligencia'), ('Telepatía', 'Telepatía'), ('Invisibilidad', 'Invisibilidad'), ('Vuelo', 'Vuelo'), ('Teletransportación', 'Teletransportación'), ('Manipulación del tiempo', 'Manipulación del tiempo'), ('Regeneración', 'Regeneración'), ('Manipulación de la energía', 'Manipulación de la energía')], max_length=50), default=list, size=None),
        ),
    ]
