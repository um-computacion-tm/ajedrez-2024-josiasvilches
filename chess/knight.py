from chess.pieces import *

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, 'Knight', row, col)
        self.white_str = '♞'
        self.black_str = '♘'

    def is_valid_move(self, row, col, board):
        # L movement
        if (abs(from_row - row) == 2 and abs(from_col - col) == 1) or (abs(from_row - row) == 1 and abs(from_col - col) == 2):
            return True
        return False
    
    def move(self, row, col):
        if self.is_valid(row, col):
            self.row = row
            self.col = col
            return True
        return False
    