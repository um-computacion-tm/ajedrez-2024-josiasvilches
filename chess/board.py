from chess.king import *
from chess.queen import *
from chess.bishop import *
from chess.rook import *
from chess.knight import *
from chess.pawn import *
from chess.exceptions import InvalidMoveError
from chess.pieces import *
from chess.movements import *

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.turn = "White"  # White starts
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

    def alternate_turn(self):
        self.turn = "White" if self.turn == "Black" else "Black"
        print(f"Es el turno de {self.turn}")
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Verificar que las coordenadas estén dentro de los límites del tablero
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            return False
        # Verificar si la casilla de destino está vacía o tiene una pieza enemiga
        destination_piece = self.get_piece(to_row, to_col)
        origin_piece = self.get_piece(from_row, from_col)

        if destination_piece is None:
            return True  # Movimiento válido si la casilla está vacía
        elif destination_piece.get_color() != origin_piece.get_color():
            return True  # Movimiento válido si es una pieza enemiga

        return False  # Movimiento no válido si es una pieza aliada
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece:
            self.__positions__[to_row][to_col] = piece
            self.__positions__[from_row][from_col] = None
            piece.set_position(to_row, to_col)

        print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")
        self.alternate_turn()
    
     # Método para mostrar el tablero
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
