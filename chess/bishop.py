from chess.pieces import *

class Bishop(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Bishop', fila, columna)

    def is_valid(self, fila, columna):
        if abs(self.fila - fila) == abs(self.columna - columna):
            return True
        return False
    
    def move(self, fila, columna):
        if self.is_valid(fila, columna):
            self.fila = fila
            self.columna = columna
            return True
        return False
    
    def __str__(self):
        if self.get_color() == 'White':
            return 'B'
        else:
            return 'b'
    