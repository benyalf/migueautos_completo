# Generated by Django 4.1 on 2022-09-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0004_alter_insumo_nombre_alter_marca_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
    ]