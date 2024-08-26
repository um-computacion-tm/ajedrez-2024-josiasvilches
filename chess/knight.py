from chess.pieces import *

class Knight(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Knight', fila, columna)
    