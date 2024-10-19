from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pieces import *

class MovementRules:

    # Direcciones generales
    STRAIGHT_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Vertical y horizontal
    DIAGONAL_DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonales
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    @staticmethod
    def get_possible_moves(piece, board):
        if isinstance(piece, Rook):
            return MovementRules.__get_rook_moves(piece, board)
        elif isinstance(piece, Bishop):
            return MovementRules.__get_bishop_moves(piece, board)
        elif isinstance(piece, Queen):
            return MovementRules.__get_queen_moves(piece, board)
        elif isinstance(piece, Knight):
            return MovementRules.__get_knight_moves(piece, board)
        elif isinstance(piece, King):
            return MovementRules.__get_king_moves(piece, board)
        elif isinstance(piece, Pawn):
            return MovementRules.__get_pawn_moves(piece, board)
        else:
            return []

    @staticmethod
    def is_valid_move(board, piece, from_row, from_col, to_row, to_col):
        piece_type = piece.get_name()
        if piece_type in ["Rook", "Bishop", "Queen"]:
            return MovementRules.is_valid_straight_or_diagonal_move(board, piece_type, from_row, from_col, to_row, to_col)
        else:
            return MovementRules.is_valid_specific_piece_move(board, piece, from_row, from_col, to_row, to_col)

    @staticmethod
    def is_valid_straight_or_diagonal_move(board, piece_type, from_row, from_col, to_row, to_col):
        if piece_type == "Rook":
            return MovementRules.is_valid_rook_move(board, from_row, from_col, to_row, to_col)
        elif piece_type == "Bishop":
            return MovementRules.is_valid_bishop_move(board, from_row, from_col, to_row, to_col)
        elif piece_type == "Queen":
            return MovementRules.is_valid_queen_move(board, from_row, from_col, to_row, to_col)
        return False

    @staticmethod
    def is_valid_specific_piece_move(board, piece, from_row, from_col, to_row, to_col):
        piece_type = piece.get_name()
        if piece_type == "Knight":
            return MovementRules.is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece_type == "King":
            return MovementRules.is_valid_king_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Pawn":
            return MovementRules.is_valid_pawn_move(board, piece, from_row, from_col, to_row, to_col)
        return False

    @staticmethod
    def is_valid_rook_move(board, from_row, from_col, to_row, to_col):
        return MovementRules.is_valid_straight_line_move(from_row, from_col, to_row, to_col) and \
               MovementRules.is_path_clear(board, from_row, from_col, to_row, to_col)

    @staticmethod
    def is_valid_bishop_move(board, from_row, from_col, to_row, to_col):
        return MovementRules.is_valid_diagonal_move(from_row, from_col, to_row, to_col) and \
               MovementRules.is_path_clear(board, from_row, from_col, to_row, to_col)

    @staticmethod
    def is_valid_queen_move(board, from_row, from_col, to_row, to_col):
        return (MovementRules.is_valid_straight_line_move(from_row, from_col, to_row, to_col) or \
                MovementRules.is_valid_diagonal_move(from_row, from_col, to_row, to_col)) and \
               MovementRules.is_path_clear(board, from_row, from_col, to_row, to_col)

    @staticmethod
    def is_valid_knight_move(from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_valid_king_move(from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return row_diff <= 1 and col_diff <= 1

    @staticmethod
    def is_valid_pawn_move(board, piece, from_row, from_col, to_row, to_col):
        turn = piece.get_color()
        direction = -1 if turn == 'White' else 1  # Blancos se mueven hacia arriba, Negros hacia abajo
        start_row = 6 if turn == 'White' else 1  # Fila de inicio de peones

        if MovementRules._is_valid_pawn_forward_move(board, from_row, from_col, to_row, to_col, direction, start_row):
            return True

        if MovementRules._is_valid_pawn_capture(board, from_row, from_col, to_row, to_col, direction):
            return True

        return False

    @staticmethod
    def _is_valid_pawn_forward_move(board, from_row, from_col, to_row, to_col, direction, start_row):
        if from_col == to_col:
            if MovementRules._is_single_step_forward(board, from_row, to_row, direction, to_col):
                return True
            if MovementRules._is_double_step_forward(board, from_row, to_row, direction, start_row, to_col):
                return True
        return False

    @staticmethod
    def _is_single_step_forward(board, from_row, to_row, direction, to_col):
        if from_row + direction == to_row:
            if board.get_piece(to_row, to_col) is None:
                return True
        return False

    @staticmethod
    def _is_double_step_forward(board, from_row, to_row, direction, start_row, to_col):
        if from_row == start_row and from_row + 2 * direction == to_row:
            if board.get_piece(to_row, to_col) is None and board.get_piece(from_row + direction, to_col) is None:
                return True
        return False

    @staticmethod
    def _is_valid_pawn_capture(board, from_row, from_col, to_row, to_col, direction):
        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.get_color() != board.get_turn():
                return True
        return False

    @staticmethod
    def is_valid_straight_line_move(from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col

    @staticmethod
    def is_valid_diagonal_move(from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)

    @staticmethod
    def is_path_clear(board, from_row, from_col, to_row, to_col):
        if from_row == to_row:
            return MovementRules.is_path_clear_horizontal(board, from_row, from_col, to_col)
        elif from_col == to_col:
            return MovementRules.is_path_clear_vertical(board, from_row, from_col, to_row)
        elif abs(from_row - to_row) == abs(from_col - to_col):
            return MovementRules.is_path_clear_diagonal(board, from_row, from_col, to_row, to_col)
        return False

    @staticmethod
    def is_path_clear_horizontal(board, from_row, from_col, to_col):
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col, step):
            if board.get_piece(from_row, col) is not None:
                return False
        return True

    @staticmethod
    def is_path_clear_vertical(board, from_row, from_col, to_row):
        step = 1 if to_row > from_row else -1
        for row in range(from_row + step, to_row, step):
            if board.get_piece(row, from_col) is not None:
                return False
        return True

    @staticmethod
    def is_path_clear_diagonal(board, from_row, from_col, to_row, to_col):
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if board.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        return True