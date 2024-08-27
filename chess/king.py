from chess.pieces import *

class King(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'King', fila, columna)
    
    # def __str__(self):
    #     if self.__color__ == 'White':
    #         return 'K'
    #     else:
    #         return 'k'