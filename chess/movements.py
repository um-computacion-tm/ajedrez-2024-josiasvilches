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
    def get_possible_moves(piece, board):
        if isinstance(piece, Rook):
            return MovementRules.is_valid_rook_move(piece, board)
        elif isinstance(piece, Bishop):
            return MovementRules.is_valid_bishop_move(piece, board)
        elif isinstance(piece, Queen):
            return MovementRules.is_valid_queen_move(piece, board)
        elif isinstance(piece, Knight):
            return MovementRules.is_valid_knight_move(piece, board)
        elif isinstance(piece, King):
            return MovementRules.is_valid_king_move(piece, board)
        elif isinstance(piece, Pawn):
            return MovementRules.is_valid_pawn_move(piece, board)
        else:
            return []

    @staticmethod
    def is_valid_move(context):
        piece_type = context.piece.get_name()
        if piece_type in ["Rook", "Bishop", "Queen"]:
            return MovementRules.is_valid_straight_or_diagonal_move(context)
        else:
            return MovementRules.is_valid_specific_piece_move(context)

    @staticmethod
    def is_valid_straight_or_diagonal_move(context):
        piece_type = context.piece.get_name()
        if piece_type == "Rook":
            return MovementRules.is_valid_rook_move(context)
        elif piece_type == "Bishop":
            return MovementRules.is_valid_bishop_move(context)
        elif piece_type == "Queen":
            return MovementRules.is_valid_queen_move(context)
        return False

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

    def is_valid_rook_move(context):
        if context.from_row == context.to_row:
            # Movimiento horizontal
            return is_path_clear_linear(context.board, context.from_row, context.from_col, context.to_col, is_horizontal=True)
        elif context.from_col == context.to_col:
            # Movimiento vertical
            return is_path_clear_linear(context.board, context.from_col, context.from_row, context.to_row, is_horizontal=False)
        return False

    @staticmethod
    def is_valid_bishop_move(context):
        return MovementRules.is_valid_diagonal_move(context) and \
               is_path_clear_diagonal(context.board, context.from_row, context.from_col, context.to_row, context.to_col)

    @staticmethod
    def is_valid_queen_move(context):
        if MovementRules.is_valid_straight_line_move(context):
            is_horizontal = context.from_row == context.to_row
            return is_path_clear_linear(context.board, context.from_row, context.from_col, context.to_col, is_horizontal)
        elif abs(context.from_row - context.to_row) == abs(context.from_col - context.to_col):
            return is_path_clear_diagonal(context.board, context.from_row, context.from_col, context.to_row, context.to_col)
        return False




    @staticmethod
    def is_valid_knight_move(context):
        row_diff = abs(context.from_row - context.to_row)
        col_diff = abs(context.from_col - context.to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_valid_king_move(context):
        row_diff = abs(context.from_row - context.to_row)
        col_diff = abs(context.from_col - context.to_col)
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
        if context.from_col == context.to_col:
            if is_single_step_forward(context, direction):
                return True
            if is_double_step_forward(context, direction, start_row):
                return True
        return False

    @staticmethod
    def _is_valid_pawn_capture(context, direction):
        if abs(context.from_col - context.to_col) == 1 and context.from_row + direction == context.to_row:
            target_piece = context.board.get_piece(context.to_row, context.to_col)
            if target_piece is not None and target_piece.get_color() != context.board.get_turn():
                return True
        return False

    @staticmethod
    def is_valid_straight_line_move(context):
        return context.from_row == context.to_row or context.from_col == context.to_col

    @staticmethod
    def is_valid_diagonal_move(context):
        return abs(context.from_row - context.to_row) == abs(context.from_col - context.to_col)
    