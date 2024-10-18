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
            return MovementRules.__traverse_directions(piece, board, MovementRules.STRAIGHT_DIRECTIONS)
        elif isinstance(piece, Bishop):
            return MovementRules.__traverse_directions(piece, board, MovementRules.DIAGONAL_DIRECTIONS)
        elif isinstance(piece, Queen):
            return MovementRules.__traverse_directions(piece, board, 
                MovementRules.STRAIGHT_DIRECTIONS + MovementRules.DIAGONAL_DIRECTIONS)
        elif isinstance(piece, Knight):
            return MovementRules.__single_step_moves(piece, board, MovementRules.KNIGHT_MOVES)
        elif isinstance(piece, King):
            return MovementRules.__single_step_moves(piece, board, 
                MovementRules.STRAIGHT_DIRECTIONS + MovementRules.DIAGONAL_DIRECTIONS)
        elif isinstance(piece, Pawn):
            return MovementRules.__get_pawn_moves(piece, board)
        else:
            return []

    # Movimiento en línea recta (usado por la torre, alfil y reina)
    @staticmethod
    def __traverse_directions(piece, board, directions):
        possible_moves = []
        row, col = piece.get_position()

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while board.is_within_bounds(r, c):
                if board.is_empty(r, c):
                    possible_moves.append((r, c))
                elif board.is_opponent_piece(r, c, piece.get_color()):
                    possible_moves.append((r, c))
                    break  # No puede continuar más allá de una captura
                else:
                    break  # Bloqueado por una pieza aliada
                r += dr
                c += dc

        return possible_moves

    # Movimiento de un solo paso (usado por el rey y el caballo)
    @staticmethod
    def __single_step_moves(piece, board, directions):
        possible_moves = []
        row, col = piece.get_position()

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if board.is_within_bounds(r, c) and (board.is_empty(r, c) or board.is_opponent_piece(r, c, piece.get_color())):
                possible_moves.append((r, c))

        return possible_moves

    # Reglas específicas para el peón
    @staticmethod
    def __get_pawn_moves(pawn, board):
        possible_moves = []
        direction = -1 if pawn.get_color() == "White" else 1
        row, col = pawn.get_position()

        MovementRules.__add_pawn_forward_moves(pawn, board, possible_moves, direction, row, col)

        MovementRules.__add_pawn_diagonal_captures(pawn, board, possible_moves, direction, row, col)
        return possible_moves
    
    @staticmethod
    def __add_pawn_forward_moves(pawn, board, possible_moves, direction, row, col):
        if board.is_empty(row + direction, col):
            possible_moves.append((row + direction, col))
            # Movimiento doble si está en la fila inicial
            if (pawn.get_color() == "White" and row == 6) or (pawn.get_color() == "Black" and row == 1):
                if board.is_empty(row + 2 * direction, col):
                    possible_moves.append((row + 2 * direction, col))

    @staticmethod
    def __add_pawn_diagonal_captures(pawn, board, possible_moves, direction, row, col):
        for dc in [-1, 1]:
            if board.is_within_bounds(row + direction, col + dc) and board.is_opponent_piece(row + direction, col + dc, pawn.get_color()):
                possible_moves.append((row + direction, col + dc))