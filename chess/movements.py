from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King


class MovementRules:

    @staticmethod
    def get_pawn_moves(pawn, board):
        row, col = pawn.get_position()
        moves = []
        direction = -1 if pawn.get_color() == "White" else 1
        
        # Movimiento hacia adelante
        if board.get_piece(row + direction, col) is None:
            moves.append((row + direction, col))

            # Movimiento de dos casillas desde la posición inicial
            if (pawn.get_color() == "White" and row == 6) or (pawn.get_color() == "Black" and row == 1):
                if board.get_piece(row + 2 * direction, col) is None:
                    moves.append((row + 2 * direction, col))

        # Capturas diagonales
        if col - 1 >= 0 and board.get_piece(row + direction, col - 1) is not None and board.get_piece(row + direction, col - 1).get_color() != pawn.get_color():
            moves.append((row + direction, col - 1))
        if col + 1 < 8 and board.get_piece(row + direction, col + 1) is not None and board.get_piece(row + direction, col + 1).get_color() != pawn.get_color():
            moves.append((row + direction, col + 1))
        
        return moves

    @staticmethod
    def get_rook_moves(rook, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Vertical y horizontal
        return rook.traverse_directions(directions, board)

    @staticmethod
    def get_bishop_moves(bishop, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]  # Diagonales
        return bishop.traverse_directions(directions, board)

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
        row, col = king.get_position()
        moves = []
        possible_moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]
        
        for r, c in possible_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.get_piece(r, c)
                if piece is None or piece.get_color() != king.get_color():
                    moves.append((r, c))
        
        return moves

    @staticmethod
    def get_possible_moves(piece, board):
        """Devuelve los movimientos posibles según el tipo de pieza."""
        if isinstance(piece, Pawn):
            return MovementRules.get_pawn_moves(piece, board)
        elif isinstance(piece, Rook):
            return MovementRules.get_rook_moves(piece, board)
        elif isinstance(piece, Knight):
            return MovementRules.get_knight_moves(piece, board)
        elif isinstance(piece, Bishop):
            return MovementRules.get_bishop_moves(piece, board)
        elif isinstance(piece, Queen):
            return MovementRules.get_queen_moves(piece, board)
        elif isinstance(piece, King):
            return MovementRules.get_king_moves(piece, board)
        else:
            return []
