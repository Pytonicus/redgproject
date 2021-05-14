# Generated by Django 3.2.3 on 2021-05-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrojuegos', '0007_alter_videojuego_lanzamiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistema',
            name='descarga',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='descarga',
            field=models.URLField(blank=True, null=True, verbose_name='Link de descarga'),
        ),
    ]
