from chess.pieces import *

class King(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'King', fila, columna)
        self.white_str = '♚'
        self.black_str = '♔'

    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.get_position()
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True
        return False
    def move(self, to_row, to_col):
        self.set_position(to_row, to_col)
        return True    