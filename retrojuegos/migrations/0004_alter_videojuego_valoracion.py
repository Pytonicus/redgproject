# Generated by Django 3.2.2 on 2021-05-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrojuegos', '0003_rename_juegoretro_videojuego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='valoracion',
            field=models.FloatField(blank=True, null=True, verbose_name='Valoración'),
        ),
    ]