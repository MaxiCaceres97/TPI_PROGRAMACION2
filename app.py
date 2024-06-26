from jugador import Jugador
from datos import *
from tablero import Tablero
from pieza import Pieza
from juego import *

# Crear tablero
tablero = Tablero()

# Inicializar el tablero con las piezas en sus posiciones iniciales
tablero.inicializar_tablero()

# Obtener una pieza en una posición específica
posicion_ejemplo = (7, 5)  # Ejemplo de posición
pieza = tablero.obtener_pieza(posicion_ejemplo[0], posicion_ejemplo[1])

if pieza:
    print(f"Pieza en posición {posicion_ejemplo}: {pieza}")
else:
    print(f"No hay pieza en la posición {posicion_ejemplo}")

