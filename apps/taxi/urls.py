from django.urls import path
from .views import CrearViaje, ListarViajes, EditarViaje, EliminarViaje, CrearVehiculo, ListarVehiculos, EditarVehiculo, EliminarVehiculo, CrearDestinosFavoritos, ListarDestinosFavoritos, EditarDestinosFavoritos, EliminarDestinosFavoritos
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar_viajes/', login_required(ListarViajes.as_view()), name='listar_viajes'),
    path('crear_viaje/', CrearViaje.as_view(), name='crear_viaje'), 
    path('editar_viaje/<int:pk>', EditarViaje.as_view(), name = 'editar_viaje'),
    path('eliminar_viaje/<int:pk>', EliminarViaje.as_view(), name = 'eliminar_viaje'), 
    path('listar_vehiculos/', login_required(ListarVehiculos.as_view()), name ='listar_vehiculos'),
    path('crear_vehiculos/', CrearVehiculo.as_view(), name = 'crear_vehiculo'),
    path('editar_vehiculo/<int:pk>', EditarVehiculo.as_view(), name='editar_vehiculo' ),
    path('eliminar_vehiculo/<int:pk>', EliminarVehiculo.as_view(), name='eliminar_vehiculo' ),
    path('listar_destinosfavoritos/',login_required(ListarDestinosFavoritos.as_view()), name = 'listar_destinosfavoritos'),
    path('crear_destinosfavoritos/', CrearDestinosFavoritos.as_view(), name = 'crear_destinosfavoritos'),
    path('editar_destinosfavoritos/<int:pk>', EditarDestinosFavoritos.as_view(), name='editar_destinosfavoritos' ),
    path('eliminar_destinosfavoritos/<int:pk>', EliminarDestinosFavoritos.as_view(), name='eliminar_destinosfavoritos' )
        
]
