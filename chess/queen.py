from chess.pieces import *

class Queen(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Queen', fila, columna)

    
    # def __str__(self):
    #     if self.__color__ == 'White':
    #         return 'Q'
    #     else:
    #         return 'q'
    # hacer el método de definir dependiendo del color (eso en piece) en la pieza solo poner White_str y black_str


