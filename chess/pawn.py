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
        if start_columna == end_columna:
            if (end_fila - start_fila) == direction:
                return True
            # Movimiento inicial de dos pasos hacia adelante
            if not self.__has_moved__ and (end_fila - start_fila) == 2 * direction:
                return True
        
        # Movimiento de captura diagonal
        if abs(start_columna - end_columna) == 1 and (end_fila - start_fila) == direction:
            if board[end_fila][end_columna] is not None and board[end_fila][end_columna].get_color() != self.get_color():
                return True
    

            return False

    def move(self, end_fila, end_columna):
        self.__has_moved__ = True
        self.set_position(end_fila, end_columna)