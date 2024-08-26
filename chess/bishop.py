from chess.pieces import *

class Bishop(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Bishop', fila, columna)