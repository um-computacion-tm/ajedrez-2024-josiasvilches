from chess.pieces import *

class Rook(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, 'Rook', row, col)
        self.white_str = '♜'
        self.black_str = '♖'
    
    def posible_positions(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            possibles.append((next_row, col))
        return possibles