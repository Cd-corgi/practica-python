# Generated by Django 4.0.2 on 2023-01-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_alter_departamentos_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terceros',
            name='correoContacto',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Contacto'),
        ),
        migrations.AlterField(
            model_name='terceros',
            name='nombreContacto',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='nombreContacto'),
        ),
    ]