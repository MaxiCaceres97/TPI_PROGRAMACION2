from pieza import Pieza

class Tablero:

    def __init__(self):
        # lista que crea una lista de 8 elementos, cada uno inicializado como None,
        # y luego repite este proceso 8 veces para formar una matriz 8x8.
        self.casillas = [[None] * 8 for _ in range(8)] 

    def inicializar_tablero(self):
        # Colocar piezas blancas
        self.casillas[0][0] = Pieza("blanca", "torre")
        self.casillas[0][1] = Pieza("blanca", "caballo")
        self.casillas[0][2] = Pieza("blanca", "alfil")
        self.casillas[0][3] = Pieza("blanca", "reina")
        self.casillas[0][4] = Pieza("blanca", "rey")
        self.casillas[0][5] = Pieza("blanca", "alfil")
        self.casillas[0][6] = Pieza("blanca", "caballo")
        self.casillas[0][7] = Pieza("blanca", "torre")
        self.casillas[1] = [Pieza("blanca", "peon") for _ in range(8)]

        # Colocar piezas negras
        self.casillas[7][0] = Pieza("negra", "torre")
        self.casillas[7][1] = Pieza("negra", "caballo")
        self.casillas[7][2] = Pieza("negra", "alfil")
        self.casillas[7][3] = Pieza("negra", "reina")
        self.casillas[7][4] = Pieza("negra", "rey")
        self.casillas[7][5] = Pieza("negra", "alfil")
        self.casillas[7][6] = Pieza("negra", "caballo")
        self.casillas[7][7] = Pieza("negra", "torre")
        self.casillas[6] = [Pieza("negra", "peon") for _ in range(8)]

    def obtener_pieza(self, fila, columna):
        # Método para obtener la pieza en una posición específica del tablero
        return self.casillas[fila][columna]