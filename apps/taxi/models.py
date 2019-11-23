from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=False, null=False)
    usuario = models.ManyToManyField(User)
    #usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'TipoUsuario'
        verbose_name_plural= 'TiposUsuarios'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name= 'Vehiculo'
        verbose_name_plural= 'Vehiculos'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class DestinoFavorito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name= 'DestinoFavorito'
        verbose_name_plural= 'DestinosFavoritos'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class Viaje(models.Model):
    id = models.AutoField(primary_key=True)
    pasajero = models.ForeignKey('auth.user', on_delete=models.CASCADE,related_name='pasajero')
    origen = models.CharField(max_length=100, blank=False, null=False)
    destino = models.CharField(max_length=100, blank=False, null=False)
    fecha_registro = models.DateTimeField(default = timezone.now)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    conductor = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='conductor')
    puntaje = models.CharField(max_length=10, blank=False, null=False)
    estado = models.CharField(max_length=50, blank=False, null=False)

    def publish(self):
        self.fecha_Registro = timezone.now()
        self.save()
    conductor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    
    def publish(self):
        self.fecha = timezone.now()
        self.save()

    class Meta:
        verbose_name= 'Viaje'
        verbose_name_plural= 'Viajes'
        ordering = ['fecha_registro']

    def __str__(self):
        return self.fecha_registro