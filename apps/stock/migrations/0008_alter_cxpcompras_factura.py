# Generated by Django 4.0.2 on 2023-01-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_alter_ingreso_consecutivo_alter_ingreso_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cxpcompras',
            name='factura',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Factura:'),
        ),
    ]