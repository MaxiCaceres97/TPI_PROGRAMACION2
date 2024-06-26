from tablero import Tablero
from jugador import Jugador
from pieza import Pieza

class Juego:
    def __init__(self, jugador_blancas, jugador_negras):
        self.jugador_blancas = jugador_blancas
        self.jugador_negras = jugador_negras
        self.tablero = Tablero()

    def iniciar_juego(self):
        # Inicializar el tablero con las piezas en sus posiciones iniciales
        self.tablero.inicializar_tablero()

        # Mostrar estado inicial del tablero (opcional)
        print("Tablero inicial:")
        self.mostrar_tablero()

    def mostrar_tablero(self):
        # Método para mostrar el estado actual del tablero
        for fila in self.tablero.casillas:
            print(fila)