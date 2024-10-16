from chess.king import *
from chess.queen import *
from chess.bishop import *
from chess.rook import *
from chess.knight import *
from chess.pawn import *

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        # Posiciones iniciales de los Rooks
        self.__positions__[0][0] = Rook("Black", "Rook")
        self.__positions__[0][7] = Rook("Black", "Rook")
        self.__positions__[7][7] = Rook("White", "Rook")
        self.__positions__[7][0] = Rook("White", "Rook")

        # Posiciones iniciales de los Knights
        self.__positions__[0][1] = Knight("Black", "Knight")
        self.__positions__[0][6] = Knight("Black", "Knight")
        self.__positions__[7][1] = Knight("White", "Knight")
        self.__positions__[7][6] = Knight("White", "Knight")

        # Posiciones iniciales de los Bishops
        self.__positions__[0][2] = Bishop("Black", "Bishop")
        self.__positions__[0][5] = Bishop("Black", "Bishop")
        self.__positions__[7][2] = Bishop("White", "Bishop")
        self.__positions__[7][5] = Bishop("White", "Bishop")

        # Posiciones iniciales de la reina
        self.__positions__[0][3] = Queen("Black", "Queen")
        self.__positions__[7][3] = Queen("White", "Queen")

        # Posiciones iniciales del rey
        self.__positions__[0][4] = King("Black", "King")
        self.__positions__[7][4] = King("White", "King")

        # Posiciones iniciales de los peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("Black", "Pawn")
            self.__positions__[6][i] = Pawn("White", "Pawn")

    
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def set_position(self, row, col, piece):
        self.__positions__[row][col] = piece
    
    def display_board(self):
        print("  a b c d e f g h")  # Etiquetas de columnas
        print(" +-----------------+")
        for row in range(8):
            row_str = f"{0 + row}|"  # Etiquetas de filas
            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    row_str += ". "  # Espacio vacío
                else:
                    row_str += str(piece) + " "
            row_str += f"|{0 + row}"
            print(row_str)
        print(" +-----------------+")
        print("  a b c d e f g h")  # Etiquetas de columnas
