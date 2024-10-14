from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pieces import *

class MovementRules():

    @staticmethod
    def get_pawn_moves(pawn, board):
        possible_moves = []
        direction = -1 if pawn.get_color() == "White" else 1
        row, col = pawn.get_position()

        # Movimiento hacia adelante (1 casilla)
        if board.is_empty(row + direction, col):
            possible_moves.append((row + direction, col))

            # Movimiento hacia adelante (2 casillas) desde la fila inicial solo si la primera está libre
            if (pawn.get_color() == "White" and row == 6) or (pawn.get_color() == "Black" and row == 1):
                if board.is_empty(row + 2 * direction, col):
                    possible_moves.append((row + 2 * direction, col))

        # Capturas diagonales (solo si hay una pieza del oponente)
        for dc in [-1, 1]:
            new_row = row + direction
            new_col = col + dc
            if board.is_within_bounds(new_row, new_col) and board.is_opponent_piece(new_row, new_col, pawn.get_color()):
                possible_moves.append((new_row, new_col))

        return possible_moves


    @staticmethod
    def get_bishop_moves(bishop, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]  # Diagonales
        return MovementRules.traverse_directions(bishop, directions, board)

    @staticmethod
    def get_knight_moves(knight, board):
        row, col = knight.get_position()
        moves = []
        possible_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        
        for r, c in possible_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.get_piece(r, c)
                if piece is None or piece.get_color() != knight.get_color():
                    moves.append((r, c))
        
        return moves

    @staticmethod
    def get_queen_moves(queen, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # Todas direcciones
        return queen.traverse_directions(directions, board)

    @staticmethod
    def get_king_moves(king, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_moves = MovementRules.traverse_directions(king, directions, board, limit=1)
        return possible_moves

    @staticmethod
    def get_possible_moves(piece, board):
        if piece.__class__.__name__ == 'Pawn':
            return MovementRules.get_pawn_moves(piece, board)
        elif piece.__class__.__name__ == 'Rook':
            return MovementRules.get_rook_moves(piece, board)
        elif piece.__class__.__name__ == 'Knight':
            return MovementRules.get_knight_moves(piece, board)
        elif piece.__class__.__name__ == 'Bishop':
            return MovementRules.get_bishop_moves(piece, board)
        elif piece.__class__.__name__ == 'Queen':
            return MovementRules.get_queen_moves(piece, board)
        elif piece.__class__.__name__ == 'King':
            return MovementRules.get_king_moves(piece, board)
        else:
            raise ValueError(f"Unknown piece type: {piece.__class__.__name__}")
