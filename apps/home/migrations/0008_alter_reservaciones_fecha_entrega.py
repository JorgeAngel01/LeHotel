# Generated by Django 4.1.2 on 2022-10-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_fecha_reservada_reservaciones_fecha_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]
