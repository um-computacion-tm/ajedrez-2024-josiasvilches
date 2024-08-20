from chess.pieces import *

class Pawn(Piece):
    def __init__(self, color, fila, columna):
        super().__init__(color, "Pawn", fila, columna)
        self.__has_moved__ = False

    def is_valid_move(self, end_fila, end_columna, board):
        start_fila, start_columna = self.get_position()

        direction = 1 if self.get_color() == 'White' else -1

        # Movimiento estándar de un paso hacia adelante
        if start_columna == end_columna:
            if (end_fila - start_fila) == direction:
                return True