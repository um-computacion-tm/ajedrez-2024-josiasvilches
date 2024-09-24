from chess.pieces import *

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, "Pawn", row, col)
        self.__has_moved__ = False
        self.white_str = '♟'
        self.black_str = '♙'

    def is_valid_move(self, end_row, end_col, board):
        start_row, start_col = self.get_position()

        direction = 1 if self.get_color() == 'White' else -1

        # Movimiento estándar de un paso hacia adelante
        if start_col == end_col:
            if (end_row - start_row) == direction:
                return True
        if start_col == end_col:
            if (end_row - start_row) == direction:
                return True
            # Movimiento inicial de dos pasos hacia adelante
            if not self.__has_moved__ and (end_row - start_row) == 2 * direction:
                return True
        
        # Movimiento de captura diagonal
        if abs(start_col - end_col) == 1 and (end_row - start_row) == direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].get_color() != self.get_color():
                return True
    

            return False

    def move(self, end_row, end_col):
        self.__has_moved__ = True
        self.set_position(end_row, end_col)