# Generated by Django 4.1.6 on 2023-03-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_userprofile_user_alter_userprofile_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rut',
            field=models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=20, unique=True),
        ),
    ]
