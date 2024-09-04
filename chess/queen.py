from chess.pieces import *

class Queen(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Queen', fila, columna)

    def get_moves(self, board):
        moves = []
        for i in range(1, 8):
            if self.fila + i < 8:
                if board[self.fila + i][self.columna] == None:
                    moves.append((self.fila + i, self.columna))
                elif board[self.fila + i][self.columna].color != self.color:
                    moves.append((self.fila + i, self.columna))
                    break
                else:
                    break
            else:
                break
            
    # def __str__(self):
    #     if self.__color__ == 'White':
    #         return 'Q'
    #     else:
    #         return 'q'
    # hacer el método de definir dependiendo del color (eso en piece) en la pieza solo poner White_str y black_str


