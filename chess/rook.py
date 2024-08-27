from chess.pieces import *

class Rook(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Rook', fila, columna)
    
    def __str__(self):
        if self.__color__ == 'White':
            return 'R'
        else:
            return 'r'
    
    def posible_positions(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            possibles.append((next_row, col))
        return possibles