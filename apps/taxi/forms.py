from django  import forms

from .models import TipoUsuario
from .models import Vehiculo
from .models import DestinoFavorito
from .models import Viaje

class TipoUsuarioForm (forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = {'descripcion','usuario'}

class VehiculoForm (forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields ={'usuario','descripcion','estado'}


class DestinoFavoritoForm (forms.ModelForm):
    class Meta:
        model = DestinoFavorito
        fields ={'usuario','descripcion'}

class ViajeForm (forms.ModelForm):
    class Meta:
        model = Viaje
        fields ={'pasajero','origen', 'destino','fecha_registro','fecha_inicio', 'fecha_fin', 'conductor','puntaje','estado'}
        

