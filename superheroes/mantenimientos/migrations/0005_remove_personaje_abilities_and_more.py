# Generated by Django 5.0.4 on 2024-05-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0004_habilidad_remove_personaje_ability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaje',
            name='abilities',
        ),
        migrations.RenameField(
            model_name='personaje',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.AddField(
            model_name='personaje',
            name='ability',
            field=models.CharField(choices=[('Fuerza', 'Fuerza'), ('Velocidad', 'Velocidad'), ('Inteligencia', 'Inteligencia'), ('Telepatía', 'Telepatía'), ('Invisibilidad', 'Invisibilidad'), ('Vuelo', 'Vuelo'), ('Teletransportación', 'Teletransportación'), ('Manipulación del tiempo', 'Manipulación del tiempo'), ('Regeneración', 'Regeneración'), ('Manipulación de la energía', 'Manipulación de la energía')], default='Fuerza', max_length=50),
        ),
        migrations.DeleteModel(
            name='Habilidad',
        ),
    ]
