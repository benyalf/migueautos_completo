# Generated by Django 4.1 on 2022-09-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_vehículo_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(blank=True, max_length=11, verbose_name='Numero de identificación'),
        ),
        migrations.AddField(
            model_name='vehículo',
            name='condición',
            field=models.CharField(choices=[('E', 'Exelente (E)'), ('R', 'Regular (R)'), ('B', 'Bien (B)'), ('M', 'Mal (M)')], default='B', max_length=12, verbose_name='Condición'),
        ),
        migrations.AlterField(
            model_name='vehículo',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
    ]
