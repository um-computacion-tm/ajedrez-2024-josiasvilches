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
    
    def get_piece_color(self, row, col):
        piece = self.get_piece(row, col)
        if piece is not None:
            return self.__positions__[row][col].get_color()
        return None
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            print(f"No hay pieza en posición inicial ({from_row}, {from_col})")
            return False
        
        possible_moves = piece.get_possible_moves(from_row, from_col)
        if (to_row, to_col) not in possible_moves:
            print(f"Movimiento inválido de ({from_row}, {from_col}) a ({to_row}, {to_col})")
            return False
        return True
    
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)

        if piece is None:
            raise InvalidMoveError("No hay pieza en la posición de origen.") # No hay pieza para mover
        
        if piece.get_color() != self.turn:
            raise InvalidMoveError(f"Es el turno de {self.turn}, no de {piece.get_color()}.")
        

        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            raise InvalidMoveError("Movimiento inválido.")

        target_piece = self.get_piece(to_row, to_col)

        # Si hay una pieza en la casilla de destino
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise InvalidMoveError("No se puede capturar una pieza del mismo color.")
            
        if target_piece is not None and target_piece.get_color() != piece.get_color():
            # Captura: remover la pieza de la casilla destino
            print(f"{piece.__class__.__name__} captura a {target_piece.__class__.__name__} en ({to_row}, {to_col})")
                
        # Mover la pieza
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None
        piece.set_position(to_row, to_col)

        self.alternate_turn()

        print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")
    
     # Método para mostrar el tablero
    def display_board(self):
        print("  a b c d e f g h")  # Etiquetas de columnas
        print(" +-----------------+")
        for row in range(8):
            row_str = f"{1 + row}|"  # Etiquetas de filas
            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    row_str += ". "  # Espacio vacío
                else:
                    row_str += str(piece) + " "
            row_str += f"|{1 + row}"
            print(row_str)
        print(" +-----------------+")
        print("  a b c d e f g h")  # Etiquetas de columnas
