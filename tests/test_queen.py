import unittest
from chess.queen import Queen
from chess.board import Board
from chess.utils import Position, GameContext, MoveContext
from chess.movements import MovementRules
from chess.chess import Chess

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()
        self.queen = Queen("White", "Queen")
        # Limpiar el tablero y colocar solo la reina
        self.clear_board()
        self.board.set_position(Position(7, 3), self.queen)

    def clear_board(self):
        for row in range(8):
            for col in range(8):
                self.board.set_position(Position(row, col), None)

    def test_queen_horizontal_move(self):
        from_position = Position(7, 3)
        to_position = Position(7, 5)
        context = self.create_move_context(self.queen, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_queen_vertical_move(self):
        from_position = Position(7, 3)
        to_position = Position(4, 3)
        context = self.create_move_context(self.queen, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_queen_diagonal_move(self):
        from_position = Position(7, 3)
        to_position = Position(5, 5)
        context = self.create_move_context(self.queen, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_queen_invalid_knight_move(self):
        from_position = Position(7, 3)
        to_position = Position(5, 4)
        context = self.create_move_context(self.queen, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()