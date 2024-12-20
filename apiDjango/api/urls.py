from django.urls import path, include
from . import views
from .views import ClientesListCreate, ClientesDetail, ClientesUpdate, ClientesDelete
from .views import Zonas_disponiblesListCreate, Zonas_disponiblesDetail, Zonas_disponiblesUpdate, Zonas_disponiblesDelete
from .views import Estado_reservaListCreate, Estado_reservaDetail, Estado_reservaUpdate, Estado_reservaDelete
from .views import ReservaListCreate, ReservaDetail, ReservaUpdate, ReservaDelete
from .views import Cancelar_reservaListCreate, Cancelar_reservaDetail, Cancelar_reservaUpdate, Cancelar_reservaDelete

urlpatterns = [
# Rutas para los clientes
    path('clientes/agregar',views.ClientesListCreate.as_view(), name='clientes-create'),
    path('clientes/obtener',views.ClientesDetail.as_view(), name='clientes-detail'),
    path('clientes/Actualizar',views.ClientesUpdate.as_view(), name='clientes-Update'),
    path('clientes/eliminar',views.ClientesDelete.as_view(), name='clientes-delete'),
    
# Rutas para zonas disponibles
    path('zonas_disponibles/agregar',views.Zonas_disponiblesListCreate.as_view(), name='zonas_disponibles-create'),
    path('zonas_disponiblles/obtener', views.Zonas_disponiblesDetail.as_view(), name='zonas_disponibles-detail'),
    path('zonas_disponibles/actulizar',views.Zonas_disponiblesUpdate.as_view(), name='zonas_disponibles-Update'),
    path('zonas_disponibles/eliminar',views.Zonas_disponiblesDelete.as_view(), name='zonas_disponibles-delete'),
    
# Rutas para los estados de reserva
    path('estado_reserva/agregar',views.Estado_reservaListCreate.as_view(), name='estado_reserva-create'),
    path('estado_reserva/obtener',views.Estado_reservaDetail.as_view(), name='estado_reserva-detail'),
    path('estado_reserva/actulizar',views.Estado_reservaUpdate.as_view(), name='estado_reserva-Update'),
    path('estado_reserva/eliminar',views.Estado_reservaDelete.as_view(), name='estado_reserva-delete'),

# Rutas para las reservas
    path('reservas/agregar',views. ReservaListCreate.as_view(), name='reservas-create'),
    path('reservas/obtener',views. ReservaDetail.as_view(), name='reservas-detail'),
    path('reservas/actualizar',views.ReservaUpdate.as_view(), name='reservas-Update'),
    path('reservas/eliminar',views.ReservaDelete.as_view(), name='reservas-delete'),

# Rutas Cancelar reserva
    path('cancelar_reserva/agregar',views. Cancelar_reservaListCreate.as_view(), name='cancelar_reserva-create'),
    path('cancelar_reserva/obtener', views.Cancelar_reservaDetail.as_view(), name='cancelar_reserva-detail'),
    path('cancelar_reserva/actualizar',views. Cancelar_reservaUpdate.as_view(), name='cancelar_reserva-Update'),
    path('cancelar_reserva/eliminar',views. Cancelar_reservaDelete.as_view(), name='cancelar_reserva-delete'),

]
