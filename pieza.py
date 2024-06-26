class Pieza:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

    def validar_movimiento(self, origen, destino):
        # Método para validar el movimiento de la pieza
        pass

    def __str__(self):
        return f"{self.color} {self.tipo}"