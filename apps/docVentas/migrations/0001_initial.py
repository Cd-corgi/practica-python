# Generated by Django 4.0.2 on 2023-01-18 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0003_alter_inventario_options_alter_inventario_idproducto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configuracion', '0008_alter_retencionesclientes_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CxcMovi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consecutivo', models.IntegerField()),
                ('prefijo', models.CharField(max_length=50, verbose_name='prefijo')),
                ('valor', models.FloatField()),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('fechaVencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('abono', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('valorDomicilio', models.FloatField(default=0)),
                ('valorLetras', models.CharField(max_length=250, verbose_name='Valor en letras')),
                ('observacion', models.CharField(blank=True, max_length=350, null=True, verbose_name='Observacion')),
                ('pagada', models.BooleanField(default=False)),
                ('xmlEstado', models.BooleanField(default=False)),
                ('cufe', models.CharField(blank=True, max_length=350, null=True, verbose_name='cufe')),
                ('qr', models.CharField(blank=True, max_length=350, null=True, verbose_name='qr')),
                ('statusFac', models.CharField(blank=True, max_length=350, null=True, verbose_name='statusFac')),
                ('valorReteFuente', models.FloatField(default=0)),
                ('valorReteIca', models.FloatField(default=0)),
                ('valorReteCree', models.FloatField(default=0)),
                ('despachado', models.BooleanField(default=False)),
                ('correoEnviado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configuracion.terceros')),
                ('formaPago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cxc_formaPago', to='configuracion.formapago')),
                ('numeracion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='numeracion_factura', to='configuracion.numeracion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facturas_vendedor', to='configuracion.vendedoresclientes')),
            ],
            options={
                'verbose_name': 'CxcMovi',
                'verbose_name_plural': 'CxcMovi',
            },
        ),
        migrations.CreateModel(
            name='CxcMoviDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.FloatField()),
                ('totalIva', models.FloatField()),
                ('total', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('descuento', models.FloatField(default=0)),
                ('lote', models.CharField(max_length=150, verbose_name='lote')),
                ('iva', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalle_factura', to='docVentas.cxcmovi')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.productos')),
            ],
            options={
                'verbose_name': 'CxcMoviDetalle',
                'verbose_name_plural': 'CxcMoviDetalles',
            },
        ),
    ]