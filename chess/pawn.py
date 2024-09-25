from chess.pieces import *

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, "Pawn", row, col)
        self.__has_moved__ = False
        self.white_str = '♟'
        self.black_str = '♙'

    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.get_position()
        direction = 1 if self.get_color() == 'White' else -1

        # Movimiento estándar de un paso hacia adelante
        if from_col == to_col:
            # verifies that the destination square is empty
            if board[to_row][to_col] is None:
                # one step forward
                if (to_row - from_row) == direction:
                    return True
            # Movimiento inicial de dos pasos hacia adelante
                if not self.__has_moved__ and (to_row - from_row) == 2 * direction:
                    if board[from_row + direction][from_col] is None:
                        return True
        
        # Movimiento de captura diagonal
        if abs(from_col - to_col) == 1 and (to_row - from_row) == direction:
            if board[to_row][to_col] is not None and board[to_row][to_col].get_color() != self.get_color():
                return True
    

        return False

    def move(self, to_row, to_col):
        self.__has_moved__ = True
        self.set_position(to_row, to_col)