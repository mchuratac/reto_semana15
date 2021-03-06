# Generated by Django 2.2.7 on 2019-11-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('origen', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('puntaje', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasajero', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': 'Viajes',
                'ordering': ['fecha_registro'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('usuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TipoUsuario',
                'verbose_name_plural': 'TiposUsuarios',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='DestinoFavorito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DestinoFavorito',
                'verbose_name_plural': 'DestinosFavoritos',
                'ordering': ['descripcion'],
            },
        ),
    ]
