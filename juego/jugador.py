class Jugador():
    def __init__(self, request):
        self.request = request
        self.session = request.session

        jugador = self.session.get("jugador")
        if not jugador:
            print('no existe el jugador')
            jugador = self.session["jugador"]={}
        self.jugador = jugador

    def setNombre (self, nombre):
        self.jugador['nombre'] = nombre
        self.guardarPartida()

    def setNivel(self, nivel):
        self.jugador['nivel'] = nivel
        self.guardarPartida()
    
    def setAcumulado(self, acumulado):
        self.jugador['acumulado'] = acumulado
        self.guardarPartida()

    def setNumeroPregunta(self, numero_pregunta):
        self.jugador['numero_pregunta'] = numero_pregunta
        self.guardarPartida()

    def aumentarAcumulado(self, acumulado):
        self.jugador['acumulado'] += acumulado
        self.guardarPartida()

    def gameOver(self):
        self.jugador['acumulado'] = 0
        self.jugador['nivel'] = 1
        self.guardarPartida()

    def guardarPartida(self):
        self.session["jugador"] = self.jugador
        self.session.modified = True