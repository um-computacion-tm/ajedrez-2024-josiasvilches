from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pieces import *
from chess.utils import *

class MovementRules:

    # Direcciones generales
    STRAIGHT_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Vertical y horizontal
    DIAGONAL_DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonales
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    @staticmethod
    def is_valid_move(context):
        piece_type = context.piece.get_name()

        # Para piezas que tienen movimientos en línea recta o diagonal
        if piece_type in ["Rook", "Bishop", "Queen"]:
            return MovementRules.is_valid_directional_move(context)

        # Para otras piezas con movimientos específicos
        return MovementRules.is_valid_specific_piece_move(context)
    
    @staticmethod
    def is_valid_specific_piece_move(context):
        piece_type = context.piece.get_name()
        if piece_type == "Knight":
            return MovementRules.is_valid_knight_move(context)
        elif piece_type == "King":
            return MovementRules.is_valid_king_move(context)
        elif piece_type == "Pawn":
            return MovementRules.is_valid_pawn_move(context)
        return False
    
    @staticmethod
    def is_valid_directional_move(context):
        from_pos = context.from_position
        to_pos = context.to_position
        
        if MovementRules.is_valid_straight_line_move(context):
            is_horizontal = from_pos.row == to_pos.row
            return is_path_clear_linear(context, is_horizontal)
        elif MovementRules.is_valid_diagonal_move(context):
            return is_path_clear_diagonal(context)
        return False
    
    @staticmethod
    def is_valid_rook_move(context):
        from_pos = context.from_position
        to_pos = context.to_position
        
        if from_pos.row == to_pos.row:
            # Movimiento horizontal
            return is_path_clear_linear(context, is_horizontal=True)
        elif from_pos.col == to_pos.col:
            # Movimiento vertical
            return is_path_clear_linear(context, is_horizontal=False)
        return False

    @staticmethod
    def is_valid_bishop_move(context):
        return MovementRules.is_valid_diagonal_move(context) and \
            MovementRules.is_valid_diagonal_path(context)

    @staticmethod
    def is_valid_queen_move(context):
        if MovementRules.is_valid_straight_line_move(context):
            is_horizontal = context.from_position.row == context.to_position.row
            return is_path_clear_linear(context, is_horizontal)
        elif MovementRules.is_valid_diagonal_move(context):
            return MovementRules.is_valid_diagonal_path(context)
        return False

    @staticmethod
    def is_valid_knight_move(context):
        row_diff = abs(context.from_position.row - context.to_position.row)
        col_diff = abs(context.from_position.col - context.to_position.col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_valid_king_move(context):
        row_diff = abs(context.from_position.row - context.to_position.row)
        col_diff = abs(context.from_position.col - context.to_position.col)
        return row_diff <= 1 and col_diff <= 1

    @staticmethod
    def is_valid_pawn_move(context):
        turn = context.piece.get_color()
        direction = -1 if turn == 'White' else 1  # Blancos se mueven hacia arriba, Negros hacia abajo
        start_row = 6 if turn == 'White' else 1  # Fila de inicio de peones

        if MovementRules._is_valid_pawn_forward_move(context, direction, start_row):
            return True

        if MovementRules._is_valid_pawn_capture(context, direction):
            return True

        return False

    @staticmethod
    def _is_valid_pawn_forward_move(context, direction, start_row):
        if context.from_position.col == context.to_position.col:
            if is_single_step_forward(context, direction):
                return True
            if is_double_step_forward(context, direction, start_row):
                return True
        return False

    @staticmethod
    def _is_valid_pawn_capture(context, direction):
        # Verifica si el movimiento de captura del peón es válido.
        if abs(context.from_position.col - context.to_position.col) == 1 and context.from_position.row + direction == context.to_position.row:
            target_piece = context.game_context.board.get_piece(context.to_position)
            if target_piece is not None and target_piece.get_color() != context.piece.get_color():
                return True
        return False

    @staticmethod
    def is_valid_straight_line_move(context):
        return context.from_position.row == context.to_position.row or context.from_position.col == context.to_position.col

    @staticmethod
    def is_valid_diagonal_move(context):
        return abs(context.from_position.row - context.to_position.row) == abs(context.from_position.col - context.to_position.col)
    
    @staticmethod
    def is_valid_diagonal_path(context):
        return is_path_clear_diagonal(context)