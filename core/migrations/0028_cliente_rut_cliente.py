# Generated by Django 4.1.7 on 2023-04-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_clienteempresa_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='rut_cliente',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
