# Generated by Django 3.0.5 on 2020-06-29 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_auto_20200628_2109'),
        ('controlop', '0002_auto_20200608_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revision_compra',
            old_name='compras_id',
            new_name='Compra',
        ),
        migrations.AddField(
            model_name='revision_produccion',
            name='Produccion_de_lote',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='produccion.Produccion_de_lote'),
            preserve_default=False,
        ),
    ]
