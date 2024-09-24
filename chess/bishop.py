from chess.pieces import *

class Bishop(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, 'Bishop', row, col)
        self.white_str = '♝'
        self.black_str = '♗'

    def is_valid(self, row, col):
        if abs(self.row - row) == abs(self.col - col):
            return True
        return False
    
    def move(self, row, col):
        if self.is_valid(row, col):
            self.row = row
            self.col = col
            return True
        return False
