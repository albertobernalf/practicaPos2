# Generated by Django 2.1.15 on 2024-06-25 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('planta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plid1', to='sitios.SedesClinica'),
        ),
        migrations.AddField(
            model_name='planta',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento'),
        ),
        migrations.AddField(
            model_name='perfilesplanta',
            name='planta',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta'),
        ),
        migrations.AddField(
            model_name='perfilesplanta',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.SedesClinica'),
        ),
        migrations.AddField(
            model_name='perfilesplanta',
            name='tiposPlanta',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.TiposPlanta'),
        ),
    ]
