from django.urls import path
from .views import configurar, agregar, leer, actualizar, borrar, jugar, validarRespuesta, gameOver, win

urlpatterns = [
    path('configurar/', configurar, name='config'),
    path('configurar/agregar/', agregar, name='agregar'),
    path('configurar/leer/<int:id_pregunta>', leer, name='leer'),
    path('configurar/actualizar/<int:id_pregunta>', actualizar, name='actualizar'),
    path('configurar/borrar/<int:id_pregunta>', borrar, name='borrar'),
    path('jugar/', jugar, name='jugar'),
    path('validarRespuesta/', validarRespuesta, name='validar'),
    path('gameOver/', gameOver, name='gameOver'),
    path('win/', win, name='win')
]
