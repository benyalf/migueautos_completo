# Generated by Django 4.1 on 2022-09-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0003_remove_insumo_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='nombre',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]