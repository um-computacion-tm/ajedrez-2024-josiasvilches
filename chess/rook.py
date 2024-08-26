from chess.pieces import *

class Rook(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Rook', fila, columna)