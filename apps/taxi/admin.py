from django.contrib import admin
from .models import TipoUsuario, Vehiculo, DestinoFavorito, Viaje

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Vehiculo)
admin.site.register(DestinoFavorito)
admin.site.register(Viaje)