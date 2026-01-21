from django.contrib import admin
from .models import ActividadTuristica, Reserva

@admin.register(ActividadTuristica)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'precio')
    search_fields = ('nombre', 'ubicacion')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'actividad', 'fecha_reserva', 'personas')
    list_filter = ('fecha_reserva', 'actividad')
