# Generated by Django 4.1.7 on 2023-03-28 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_rollizo_id_patron'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteempresa',
            name='fecha_crea',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clienteempresa',
            name='usuario_crea',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rollizo',
            name='clase_diametrica',
            field=models.IntegerField(blank=True, choices=[(12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30)], null=True),
        ),
    ]
