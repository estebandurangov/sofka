from django.contrib import admin
from juego.models import Categoria, Pregunta, Respuesta, Jugador

# Register your models here.

admin.site.register({Categoria, Pregunta, Respuesta, Jugador})