from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre_categoria = models.CharField(max_length=50)
    premio = models.FloatField()

    def __str__(self) -> str:
        return self.nombre_categoria

class Pregunta (models.Model):
    pregunta = models.TextField(max_length=200)
    categoria_pregunta = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.pregunta

class Respuesta (models.Model):
    respuesta = models.TextField(max_length=200)
    pregunta_respuesta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    valida = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.respuesta

class Jugador (models.Model):
    nombre = models.CharField(max_length=50)
    ganador = models.BooleanField(default=False)
    premio = models.FloatField(default=0)

    class Meta:
        ordering = ['-premio']