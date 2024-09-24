from chess.pieces import *

class King(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'King', fila, columna)
        self.white_str = '♚'
        self.black_str = '♔'

    def is_valid_move(self, end_row, end_col, board):
        start_row, start_col = self.get_position()
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return True
        return False
    def move(self, end_row, end_col):
        self.set_position(end_row, end_col)
        return True    