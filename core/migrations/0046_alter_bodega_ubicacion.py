# Generated by Django 4.1.7 on 2023-05-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_bodega_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
