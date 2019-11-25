from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TipoUsuario
from .forms import TipoUsuarioForm

from .models import Vehiculo
from .forms import VehiculoForm

from .models import DestinoFavorito
from .forms import DestinoFavoritoForm

from .models import Viaje
from .forms import ViajeForm
# Create your views here.

class home(View):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass

class Home(TemplateView):
    template_name = 'taxi/index.html'

    def get_context_data(self, *args, **kwargs):
        tipousuario = TipoUsuario.objects.prefetch_related("tipousuario").all()
        context = super(Home,self).get_context_data(*args, **kwargs)
        context['tipousuario'] = tipousuario
        return context



class ListarViajes(ListView):
    model = Viaje
    template_name =  'taxi/viaje/listar_viajes.html'    
    queryset = Viaje.objects.all()
    context_object_name = 'viajes'


class CrearViaje(CreateView):
    model = Viaje
    form_class = ViajeForm
    template_name= 'taxi/viaje/crear_viaje.html'
    success_url = reverse_lazy ('taxi:listar_viajes')



class EditarViaje(UpdateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'taxi/viaje/editar_viaje.html'
    success_url = reverse_lazy('taxi:listar_viajes')

class EliminarViaje(DeleteView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'taxi/viaje/eliminar_viaje.html'
    success_url = reverse_lazy('taxi:listar_viajes')


class ListarVehiculos(ListView):
    model =  Vehiculo
    template_name ='taxi/vehiculo/listar_vehiculos.html'
    queryset = Vehiculo.objects.all()
    context_object_name = 'vehiculos'



class CrearVehiculo(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxi/vehiculo/crear_vehiculo.html'
    success_url = reverse_lazy('taxi:listar_vehiculos')

class EditarVehiculo(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxi/vehiculo/editar_vehiculo.html'
    success_url = reverse_lazy ('taxi:listar_vehiculos')

class EliminarVehiculo(DeleteView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxi/vehiculo/eliminar_vehiculo'
    success_url = reverse_lazy ('taxi:listar_vehiculos')

    
    def get_context_data(self,*args,**kwards):
        vehiculo = Vehiculo.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarVehiculo,self).get_context_data(*args,**kwards)
        context['vehiculo'] = vehiculo



class ListarDestinosFavoritos(ListView):
    model =  DestinoFavorito
    template_name ='taxi/destinosfavoritos/listar_destinosfavoritos.html'
    queryset = DestinoFavorito.objects.all()
    context_object_name='destinosfavoritos'




class CrearDestinosFavoritos(CreateView):
    model = DestinoFavorito
    form_class = DestinoFavoritoForm
    template_name = 'taxi/destinosfavoritos/crear_destinofavorito.html'
    success_url = reverse_lazy('taxi:listar_destinosfavoritos')


class EditarDestinosFavoritos(UpdateView):
    model = DestinoFavorito
    form_class = DestinoFavoritoForm
    template_name = 'taxi/destinosfavoritos/editar_destinofavorito.html'
    success_url = reverse_lazy ('taxi:listar_destinosfavoritos')

class EliminarDestinosFavoritos(DeleteView):
    model = DestinoFavorito
    form_class = DestinoFavoritoForm
    template_name = 'taxi/destinosfavoritos/eliminar_destinofavorito.html'
    success_url = reverse_lazy ('taxi:listar_destinosfavoritos')
 

    def get_context_data(self,*args,**kwards):
        destinofavorito = DestinoFavorito.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarDestinosFavoritos,self).get_context_data(*args,**kwards)
        context['destinofavorito'] = destinofavorito














