from chess.pieces import *
from chess.utils import *

class MovementRules:

    # General directions
    STRAIGHT_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Vertical and horizontal
    DIAGONAL_DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal directions
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    @staticmethod
    def is_valid_move(context):
        """This function checks if a move is valid based on the piece type."""
        piece_type = context.piece.get_name()
        rules = MovementRules

        # Dictionary that associates pieces with their movement functions
        movements = {
            "Rook": rules.is_valid_rook_move,
            "Knight": rules.is_valid_knight_move,
            "Bishop": rules.is_valid_bishop_move,
            "Queen": rules.is_valid_queen_move,
            "King": rules.is_valid_king_move,
            "Pawn": rules.is_valid_pawn_move
        }

        # Gets the corresponding validation function
        movimiento_func = movements.get(piece_type)

        if movimiento_func:
            # Calls the corresponding function passing the context
            return movimiento_func(context)
        
        return False

    @staticmethod
    def check_horizontal_or_vertical(context, from_pos, to_pos):
        """This function checks if the move is valid and if the path is clear for straight-line movements."""
        is_horizontal = from_pos.row == to_pos.row
        if is_horizontal:
            return is_path_clear_linear(context, True)  # Horizontal move
        else:
            return is_path_clear_linear(context, False)  # Vertical move

    @staticmethod
    def is_valid_rook_move(context):
        """This function checks if the rook's movement is valid (straight lines only)."""
        return MovementRules.is_valid_straight_line_move(context) and \
            is_path_clear_linear(context, is_horizontal=(context.from_position.row == context.to_position.row))

    @staticmethod
    def is_valid_bishop_move(context):
        """This function checks if the bishop's movement is valid (diagonal moves only)."""
        return MovementRules.is_valid_diagonal_move(context) and \
            is_path_clear_diagonal(context)

    @staticmethod
    def is_valid_queen_move(context):
        """This function checks if the queen's movement is valid (combines rook and bishop moves)."""
        if MovementRules.is_valid_straight_line_move(context):
            is_horizontal = context.from_position.row == context.to_position.row
            return is_path_clear_linear(context, is_horizontal)
        elif MovementRules.is_valid_diagonal_move(context):
            return MovementRules.is_valid_diagonal_path(context)
        return False

    @staticmethod
    def is_valid_knight_move(context):
        """This function checks if the knight's movement is valid (L-shape moves)."""
        row_diff = abs(context.from_position.row - context.to_position.row)
        col_diff = abs(context.from_position.col - context.to_position.col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_valid_king_move(context):
        """This function checks if the king's movement is valid (one square in any direction)."""
        row_diff = abs(context.from_position.row - context.to_position.row)
        col_diff = abs(context.from_position.col - context.to_position.col)
        return row_diff <= 1 and col_diff <= 1

    @staticmethod
    def is_valid_pawn_move(context):
        """This function checks if the pawn's movement is valid (forward moves and captures)."""
        turn = context.piece.get_color()
        direction = -1 if turn == 'White' else 1  # Whites move up, Blacks move down
        start_row = 6 if turn == 'White' else 1  # Starting row for pawns

        if MovementRules._is_valid_pawn_forward_move(context, direction, start_row):
            return True

        if MovementRules._is_valid_pawn_capture(context, direction):
            return True

        return False

    @staticmethod
    def _is_valid_pawn_forward_move(context, direction, start_row):
        """This function checks if the pawn's forward movement is valid (single or double step)."""
        if context.from_position.col == context.to_position.col:
            if is_single_step_forward(context, direction):
                return True
            if is_double_step_forward(context, direction, start_row):
                return True
        return False

    @staticmethod
    def _is_valid_pawn_capture(context, direction):
        """This function checks if the pawn's capture move is valid."""
        if abs(context.from_position.col - context.to_position.col) == 1 and context.from_position.row + direction == context.to_position.row:
            target_piece = context.game_context.board.get_piece(context.to_position)
            if target_piece is not None and target_piece.get_color() != context.piece.get_color():
                return True
        return False

    @staticmethod
    def is_valid_straight_line_move(context):
        """This function checks if the move is a straight line (horizontal or vertical)."""
        return context.from_position.row == context.to_position.row or context.from_position.col == context.to_position.col

    @staticmethod
    def is_valid_diagonal_move(context):
        """This function checks if the move is a diagonal move."""
        return abs(context.from_position.row - context.to_position.row) == abs(context.from_position.col - context.to_position.col)

    @staticmethod
    def is_valid_diagonal_path(context):
        """This function checks if the diagonal path is clear for movement."""
        return is_path_clear_diagonal(context)
