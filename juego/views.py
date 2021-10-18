from typing import ClassVar
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .jugador import Jugador

from .models import Pregunta, Categoria, Respuesta
from .models import Jugador as Player
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

#esta vista nos permite editar, eliminar o agregar preguntas a nuestro juego
@login_required(login_url='/admin')
def configurar(request):
    categorias = Categoria.objects.all()
    preguntas = Pregunta.objects.all()
    jugadores = Player.objects.all()
    context = {
        'CATEGORIAS':categorias,
        'PREGUNTAS': preguntas,
        'JUGADORES': jugadores,
        }
    return render(request, 'configuracion.html', context)

@login_required(login_url='/admin')
def agregar(request):
    if (request.method == "POST"): #se verifica si hay una solicitud
        pregunta = request.POST["pregunta"]
        categoria_pregunta = Categoria.objects.get(id = request.POST["id_categoria"])
        pregunta = Pregunta(pregunta=pregunta, categoria_pregunta=categoria_pregunta)
        pregunta.save()
        respuesta = Respuesta(respuesta=request.POST['respuesta1'], pregunta_respuesta=pregunta, valida=True) #agregamos primero la respuesta correcta
        respuesta.save()
        for i in range (2,5): #agregamos las otras opciones 
            respuesta = ("respuesta"+str(i))
            respuesta = Respuesta(respuesta=request.POST[respuesta], pregunta_respuesta=pregunta)
            respuesta.save()
        messages.success(request, f"la pregunta {pregunta} se agrego correctamente")
        return redirect('config')
    redirect('config')

#esta funcion recibe como parametro una pregunta y cuando se hace la solicitud tambien recibe los elementos de la pregunta
@login_required(login_url='/admin')
def leer(request, id_pregunta):
    pregunta = Pregunta.objects.get(id=id_pregunta)
    
    categorias = Categoria.objects.all()
    respuestas = Respuesta.objects.filter(pregunta_respuesta=pregunta)
    context = {
        'pregunta':pregunta,
        'RESPUESTAS': respuestas,
        'CATEGORIAS': categorias,
    }
    return render(request, 'editarPregunta.html', context)

@login_required(login_url='/admin')
def actualizar(request, id_pregunta):
    try: 
        pregunta = Pregunta.objects.get(id=id_pregunta)
    except: #si el id de la pregunta no existe, entonces retornamos a la pagina de configuración con su respectivo mensaje
        messages.error(request, f"La pregunta que quiere editar no existe")
        redirect('config')

    if (request.method == "POST"):
        pregunta.pregunta = request.POST["pregunta"]
        pregunta.categoria_pregunta = Categoria.objects.get(id = request.POST["id_categoria"])
        pregunta.save()
        respuestas = Respuesta.objects.filter(pregunta_respuesta=pregunta)
        i=1
        for respuesta in respuestas:
            respuesta.respuesta = request.POST["respuesta"+str(i)]
            respuesta.save()
            i += 1
        messages.success(request, f"La pregunta {pregunta} se editó correctamente")
        return redirect('config')
    return redirect('leer', id_pregunta=id_pregunta)

@login_required(login_url='/admin')
def borrar(request, id_pregunta):
    try:
        pregunta = Pregunta.objects.get(id=id_pregunta)
    except Pregunta.DoesNotExist:
        messages.error(request, f"La pregunta que quiere eliminar no existe")
        return redirect('config')
    pregunta.delete()
    messages.success(request, f"La pregunta {pregunta} ha sido eliminada")
    return redirect('config')

def jugar(request):
    jugador = Jugador(request)
    
    if (request.method == "POST"):
        categoria = Categoria.objects.get(id=1)
        preguntas = Pregunta.objects.filter(categoria_pregunta=categoria)
        jugador.setNombre(request.POST["nombre"])
        jugador.setNivel(1)
        jugador.setAcumulado(0)
        jugador.setNumeroPregunta(random.randint(0,len(preguntas)-1))
    nivel = int(jugador.jugador['nivel'])
    categoria = Categoria.objects.get(id=nivel)
    preguntas = Pregunta.objects.filter(categoria_pregunta=categoria)
    numero_pregunta = jugador.jugador['numero_pregunta']

    pregunta = preguntas[numero_pregunta]
    respuestas = list(Respuesta.objects.filter(pregunta_respuesta=pregunta))
    random.shuffle(respuestas)
    premio_acumulado = jugador.jugador['acumulado']
    premio_acierto = premio_acumulado + categoria.premio

    context = {
        'nivel': nivel,
        'pregunta': pregunta, 
        'RESPUESTAS': respuestas,
        'acumulado': premio_acumulado,
        'premio': premio_acierto
        }
    return render(request, 'juego.html', context)
    
def validarRespuesta(request):
    if (request.method == "POST"):
        respuesta = Respuesta.objects.get(id=request.POST["opcion"])
        jugador = Jugador(request)
        if (respuesta.valida):
            nivel = int(jugador.jugador['nivel'])
            jugador.setNivel(nivel+1)
            jugador.aumentarAcumulado(Categoria.objects.get(id=nivel).premio)
            if (nivel+1 > 5):
                return redirect('win')

            categoria = Categoria.objects.get(id=nivel+1)
            numPreguntas = len(Pregunta.objects.filter(categoria_pregunta=categoria))

            jugador.setNumeroPregunta(random.randint(0,numPreguntas-1))
            
            return redirect('jugar')
        return redirect('gameOver')
    return redirect('jugar')

def gameOver(request):
    jugador = Jugador(request)
    nombre= jugador.jugador['nombre']
    jugador.gameOver()

    jugador = Player(nombre=nombre)
    jugador.save()

    messages.error(request, f"lo sentimos {nombre} has perdido")
    return redirect('inicio')

def win(request):
    jugador = Jugador(request)
    nombre= jugador.jugador['nombre']
    premio=  jugador.jugador['acumulado']
    jugador.gameOver()

    Player(nombre=nombre, premio=premio, ganador=True).save()

    messages.success(request, f"Felicitaciones {nombre}, has ganado {premio}")

    return redirect('inicio')
