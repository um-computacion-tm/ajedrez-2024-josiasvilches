from chess.pieces import *

class King(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'King', fila, columna)
    
    # def __str__(self):
    #     if self.__color__ == 'White':
    #         return 'K'
    #     else:
    #         return 'k'

    def is_valid_move(self, end_fila, end_columna, board):
        start_fila, start_columna = self.get_position()
        if abs(start_fila - end_fila) <= 1 and abs(start_columna - end_columna) <= 1:
            return True
        return False
    def move(self, end_fila, end_columna):
        self.set_position(end_fila, end_columna)