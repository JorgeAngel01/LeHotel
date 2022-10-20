# Generated by Django 4.1.2 on 2022-10-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_agregados_costo_datospago_medios_habitaciones_costo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservaciones',
            old_name='fecha_reservada',
            new_name='fecha_reserva',
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='cant_adultos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='cant_ninos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservaciones',
            name='fecha_entrega',
            field=models.DateField(default='2022-10-20'),
            preserve_default=False,
        ),
    ]