# Generated by Django 2.1.15 on 2024-06-25 13:35

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('planta', '0002_auto_20240625_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialdependencias',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentohistorialDep', to='usuarios.Usuarios'),
        ),
        migrations.AddField(
            model_name='historialdependencias',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento'),
        ),
        migrations.AddField(
            model_name='historialdependencias',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='dependencias',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Dependencias'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoDepAct', to='usuarios.Usuarios'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='dependenciasTipo',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.DependenciasTipo'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.SedesClinica'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='serviciosSedes',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='serviciosSedes1', to='sitios.ServiciosSedes'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='subServiciosSedes',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.SubServiciosSedes'),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='departamentos',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ciudades', to='sitios.Departamentos'),
        ),
        migrations.AddField(
            model_name='centros',
            name='ciudades',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='departamentos', chained_model_field='departamentos', on_delete=django.db.models.deletion.CASCADE, to='sitios.Ciudades'),
        ),
        migrations.AddField(
            model_name='centros',
            name='departamentos',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Departamentos'),
        ),
        migrations.AlterUniqueTogether(
            name='subserviciossedes',
            unique_together={('sedesClinica', 'servicios', 'subServicios')},
        ),
        migrations.AlterUniqueTogether(
            name='serviciossedes',
            unique_together={('sedesClinica', 'servicios')},
        ),
    ]
