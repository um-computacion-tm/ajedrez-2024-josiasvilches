from chess.board import Board
from chess.exceptions import InvalidMoveError


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
        self.__ganador__ = None
    
    def is_within_board_limits(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_path_clear(self, from_row, from_col, to_row, to_col):
        if from_row == to_row:
            return self.is_path_clear_horizontal(from_row, from_col, to_col)
        elif from_col == to_col:
            return self.is_path_clear_vertical(from_row, from_col, to_row)
        elif abs(from_row - to_row) == abs(from_col - to_col):
            return self.is_path_clear_diagonal(from_row, from_col, to_row, to_col)
        return False
    
    def is_path_clear_horizontal(self, from_row, from_col, to_col):
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col, step):
            if self.__board__.get_piece(from_row, col) is not None:
                return False
        return True
    
    def is_path_clear_vertical(self, from_row, from_col, to_row):
        step = 1 if to_row > from_row else -1
        for row in range(from_row + step, to_row, step):
            if self.__board__.get_piece(row, from_col) is not None:
                return False
        return True
       
    def is_path_clear_diagonal(self, from_row, from_col, to_row, to_col):
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        current_row, current_col = from_row + row_step, from_col + col_step
        while current_row != to_row and current_col != to_col:
            if self.__board__.get_piece(current_row, current_col) is not None:
                return False
            current_row += row_step
            current_col += col_step
        return True
    
    def is_valid_straight_line_move(self, from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col
    
    def is_valid_diagonal_move(self, from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)

    def move(self, from_row, from_col, to_row, to_col):
        # Obtiene la pieza a mover
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise InvalidMoveError("No hay ninguna pieza en esa posición.")
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise InvalidMoveError(f"Es el turno de {self.__turn__}, no de {piece.get_color__}.")
        # Verificar si el movimiento es válido según las reglas de la pieza
        if not self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMoveError("Movimiento no válido para la pieza seleccionada.")
        
        result = self.move_piece(from_row, from_col, to_row, to_col) # Realizar el movimiento y verificar si el rey fue capturado
        if result == "ReyEliminado":
            return "ReyEliminado"  # Enviar mensaje al main.py para finalizar el juego
        
        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()
        return "Valido"  # Movimiento realizado correctamente

    def is_valid_move(self, piece, from_row, from_col, to_row, to_col):
        piece_type = piece.get_name()
        # color = piece.get_color()
        if piece_type in ["Rook", "Bishop", "Queen"]:
            return self.is_valid_straight_or_diagonal_move(piece_type, from_row, from_col, to_row, to_col)
        else:
            return self.is_valid_specific_move(from_row, from_col, to_row, to_col, piece)
        
    def is_valid_straight_or_diagonal_move(self, piece_type, from_row, from_col, to_row, to_col):
        if piece_type == "Rook":
            return self.is_valid_straight_line_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Bishop":
            return self.is_valid_diagonal_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Queen":
            return self.is_valid_queen_move(from_row, from_col, to_row, to_col)
        return False

    def is_valid_specific_move(self, from_row, from_col, to_row, to_col, piece):
        piece_type = piece.get_name()
        if piece_type == "Knight":
            return self.is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece_type == "King":
            return self.is_valid_king_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Pawn":
            return self.is_valid_pawn_move(piece, from_row, from_col, to_row, to_col)
        return False
    
    def is_valid_knight_move(self, from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def is_valid_rook_move(self, from_row, from_col, to_row, to_col):
        return self.is_valid_straight_line_move(from_row, from_col, to_row, to_col) and \
            self.is_path_clear(from_row, from_col, to_row, to_col)

    def is_valid_bishop_move(self, from_row, from_col, to_row, to_col):
        return self.is_valid_diagonal_move(from_row, from_col, to_row, to_col) and \
            self.is_path_clear(from_row, from_col, to_row, to_col)

    def is_valid_queen_move(self, from_row, from_col, to_row, to_col):
        return (self.is_valid_straight_line_move(from_row, from_col, to_row, to_col) or \
                self.is_valid_diagonal_move(from_row, from_col, to_row, to_col)) and \
            self.is_path_clear(from_row, from_col, to_row, to_col)

    def is_valid_king_move(self, from_row, from_col, to_row, to_col):
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1
    
    def is_valid_pawn_move(self, piece, from_row, from_col, to_row, to_col):
        turn = piece.get_color()
        direction = -1 if turn == 'White' else 1  # Blancos se mueven hacia arriba, Negros hacia abajo
        start_row = 6 if turn == 'White' else 1  # Fila de inicio de peones

        if self._is_valid_pawn_forward_move(from_row, from_col, to_row, to_col, direction, start_row):
            return True

        if self._is_valid_pawn_capture(from_row, from_col, to_row, to_col, direction):
            return True

        return False
    
    def _is_valid_pawn_forward_move(self, from_row, from_col, to_row, to_col, direction, start_row):
        if from_col == to_col:
            if self._is_single_step_forward(from_row, to_row, direction, to_col):
                return True
            if self._is_double_step_forward(from_row, to_row, direction, start_row, to_col):
                return True
            return False

    def _is_single_step_forward(self, from_row, to_row, direction, to_col):
        if from_row + direction == to_row:
            if self.__board__.get_piece(to_row, to_col) is None:
                return True
        return False

    def _is_double_step_forward(self, from_row, to_row, direction, start_row, to_col):
        if from_row == start_row and from_row + 2 * direction == to_row:
            if self.__board__.get_piece(to_row, to_col) is None and self.__board__.get_piece(from_row + direction, to_col) is None:
                return True
        return False
    
    def _is_valid_pawn_capture(self, from_row, from_col, to_row, to_col, direction):
        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            target_piece = self.__board__.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.get_color() != self.__turn__:
                return True
    
        return False

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece:
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            self.__board__.set_position(from_row, from_col, None)
            print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")
        
        if self.__board__.get_piece(to_row, to_col).get_name() == "King":
            self.__ganador__ = self.__turn__
            return "ReyEliminado"
        
    def alternate_turn(self):
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__

    def display_board(self):
        self.__board__.display_board()

    def get_ganador(self):
        return self.__ganador__
