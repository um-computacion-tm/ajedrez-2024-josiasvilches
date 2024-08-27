from chess.king import *
from chess.queen import *
from chess.bishop import *
from chess.rook import *
from chess.knight import *
from chess.pawn import *

class Board:
    def __init__(self):
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        # Posiciones iniciales de los Rooks
        self.__positions__[0][0] = Rook("Black", 0, 0)
        self.__positions__[0][7] = Rook("Black", 0, 7)
        self.__positions__[7][7] = Rook("White", 7, 7)
        self.__positions__[7][0] = Rook("White", 7, 0)

        # Posiciones iniciales de los Knights
        self.__positions__[0][1] = Knight("Black", 0, 1)
        self.__positions__[0][6] = Knight("Black", 0, 6)
        self.__positions__[7][1] = Knight("White", 7, 1)
        self.__positions__[7][6] = Knight("White", 7, 6)

        # Posiciones iniciales de los Bishops
        self.__positions__[0][2] = Bishop("Black", 0, 2)
        self.__positions__[0][5] = Bishop("Black", 0, 5)
        self.__positions__[7][2] = Bishop("White", 7, 2)
        self.__positions__[7][5] = Bishop("White", 7, 5)

        # Posiciones iniciales de la reina
        self.__positions__[0][3] = Queen("Black", 0, 3)
        self.__positions__[7][3] = Queen("White", 7, 3)

        # Posiciones iniciales del rey
        self.__positions__[0][4] = King("Black", 0, 4)
        self.__positions__[7][4] = King("White", 7, 4)

        # Posiciones iniciales de los peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("Black", 1, i)
            self.__positions__[6][i] = Pawn("White", 6, i)


    def get_piece(self, row, col):
        return self.__positions__[row][col]
