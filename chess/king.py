from chess.pieces import *

class King(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'King', fila, columna)
    
