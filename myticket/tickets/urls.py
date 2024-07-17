from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/registrar/', views.registrarticket, name='registrarticket'),
    path('tickets/editar/<int:id>/', views.editarticket, name='editarticket'),
    path('tickets/eliminar/<int:id>/', views.eliminarticket, name='eliminarticket'),
]
