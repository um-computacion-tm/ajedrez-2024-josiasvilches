from chess.board import *
from chess.exceptions import InvalidMoveError
from chess.pieces import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
    
    def move(self, from_row, from_col, to_row, to_col):
        # Obtiene la pieza a mover
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise InvalidMoveError("No hay ninguna pieza en esa posición.")
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise InvalidMoveError(f"Es el turno de {self.__turn__}, no de {piece.get_color()}.")
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
        color = piece.get_color()
        if piece_type == "Rook":
            return is_valid_straight_line_move(from_row, from_col, to_row, to_col) and \
                     (is_path_clear_horizontal(from_row, from_col, to_col, self.__board__) or \
                        is_path_clear_vertical(from_row, from_col, to_row, self.__board__))
        
        elif piece_type == "Bishop":
            return is_valid_diagonal_move(from_row, from_col, to_row, to_col) and \
                        is_path_clear_diagonal(from_row, from_col, to_row, to_col, self.__board__)
        elif piece_type == "Knight":
            return self.is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Queen":
            return (is_valid_straight_line_move(from_row, from_col, to_row, to_col) and \
                    (is_path_clear_horizontal(from_row, from_col, to_col, self.__board__) or \
                    is_path_clear_vertical(from_row, from_col, to_row, self.__board__))) or \
                    (is_valid_diagonal_move(from_row, from_col, to_row, to_col) and \
                    is_path_clear_diagonal(from_row, from_col, to_row, to_col, self.__board__))
        elif piece_type == "King":
            return self.is_valid_king_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Pawn":
            return self.is_valid_pawn_move(piece, from_row, from_col, to_row, to_col, self.__board__, color)
        return False  # Si no se reconoce la pieza, el movimiento es inválido

    def is_within_board_limits(row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def is_path_clear_horizontal(from_row, from_col, to_col, board):
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col, step):
            if board.get_piece(from_row, col) is not None:
                return False
        return True

    def is_path_clear_vertical(from_row, from_col, to_row, board):
        step = 1 if to_row > from_row else -1
        for row in range(from_row + step, to_row, step):
            if board.get_piece(row, from_col) is not None:
                return False
        return True

    def is_path_clear_diagonal(from_row, from_col, to_row, to_col, board):
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        current_row, current_col = from_row + row_step, from_col + col_step
        while current_row != to_row and current_col != to_col:
            if board.get_piece(current_row, current_col) is not None:
                return False
            current_row += row_step
            current_col += col_step
        return True

    def is_valid_straight_line_move(from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col

    def is_valid_diagonal_move(from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)

    def is_valid_knight_move(self, from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    # Regla de movimiento para el rey (King)
    def is_valid_king_move(self, from_row, from_col, to_row, to_col):
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1

    # Regla de movimiento para el peón (Pawn)
    def is_valid_pawn_move(self, pawn, from_row, from_col, to_row, to_col):
        direction = 1 if pawn.get_color() == "White" else -1
        start_row = 1 if pawn.get_color() == "White" else 6
        
        if from_col == to_col:
            if from_row + direction == to_row and self.__board__.get_piece(to_row, to_col) is None: # Movimiento hacia adelante
                return True
            
            if from_row == start_row and from_row + 2 * direction == to_row and self.__board__.get_piece(to_row, to_col) is None: # Movimiento inicial doble
                return True
        
        elif abs(from_col - to_col) == 1 and from_row + direction == to_row and self.__board__.get_piece(to_row, to_col) is not None: # Captura diagonal
            return True
        
        return False  # Cualquier otro movimiento es inválido para el peón

    def move_piece(self, from_row, from_col, to_row, to_col, piece):
        """Mueve una pieza en tablero."""
        piece = self.__board__.get_piece(from_row, from_col)
        if not self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMoveError("Movimiento no válido para la pieza seleccionada.")
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        if piece:
            self.__board__.set_position(to_row, to_col, piece)
            self.__board__.set_position(from_row, from_col, None)
            print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")

        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        if self.__board__.get_piece(to_row, to_col).get_name() == "King":
            self.__ganador__ = self.__turn__
            return "ReyEliminado"
        # return "Valido"


    def move_straight_line(self, from_row, from_col, to_row, to_col, direction):
        """Mueve en línea recta (horizontal o vertical) y verifica el bloqueo."""
        if direction == "horizontal":
            return is_path_clear_horizontal(from_row, from_col, to_col, self.__board__)
        elif direction == "vertical":
            return is_path_clear_vertical(from_row, from_col, to_row, self.__board__)
        return False
    
    def move_diagonal(self, from_row, from_col, to_row, to_col):
        """Mueve en diagonal y verifica el bloqueo."""
        if not is_valid_diagonal_move(from_row, from_col, to_row, to_col):
            return False
        return is_path_clear_diagonal(from_row, from_col, to_row, to_col, self.__board__)

    def get_ganador(self):
        return self.__ganador__

    def alternate_turn(self):
        # Alternar turno entre "White" y "Black"
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__
    
    def display_board(self):
        self.__board__.display_board()
