from chess.pieces import *

class Knight(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Knight', fila, columna)

    def is_valid(self, fila, columna):
        if abs(self.fila - fila) == 2 and abs(self.columna - columna) == 1:
            return True
        if abs(self.fila - fila) == 1 and abs(self.columna - columna) == 2:
            return True
        return False
    
    def move(self, fila, columna):
        if self.is_valid(fila, columna):
            self.fila = fila
            self.columna = columna
            return True
        return False
    
    