from chess.pieces import *

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, 'Queen', row, col)
        self.white_str = '♛'
        self.black_str = '♕'

    def get_moves(self, board):
        moves = []
        for i in range(1, 8):
            if self.row + i < 8:
                if board[self.row + i][self.col] == None:
                    moves.append((self.row + i, self.col))
                elif board[self.row + i][self.col].color != self.color:
                    moves.append((self.row + i, self.col))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if self.row - i >= 0:
                if board[self.row - i][self.col] == None:
                    moves.append((self.row - i, self.col))
                elif board[self.row - i][self.col].color != self.color:
                    moves.append((self.row - i, self.col))
                    break
                else:
                    break
            else:
                break
