# Generated by Django 4.1 on 2022-09-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0006_alter_marca_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
    ]