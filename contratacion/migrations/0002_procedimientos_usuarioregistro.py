# Generated by Django 2.1.15 on 2024-06-25 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planta', '0001_initial'),
        ('contratacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimientos',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta'),
        ),
    ]
