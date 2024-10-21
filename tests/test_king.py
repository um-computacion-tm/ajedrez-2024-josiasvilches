import unittest
from chess.king import King
from chess.queen import Queen
from chess.board import Board
from chess.utils import Position, GameContext, MoveContext
from chess.movements import MovementRules
from chess.chess import Chess
from chess.exceptions import KingisDeadException

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()
        self.king = King("White", "King")
        self.board.set_position(Position(7, 4), self.king)

    def test_king_single_step_horizontal(self):
        from_position = Position(7, 4)
        to_position = Position(7, 5)
        context = self.create_move_context(self.king, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_king_single_step_vertical(self):
        from_position = Position(7, 4)
        to_position = Position(6, 4)
        context = self.create_move_context(self.king, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_king_single_step_diagonal(self):
        from_position = Position(7, 4)
        to_position = Position(6, 5)
        context = self.create_move_context(self.king, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_king_invalid_two_steps(self):
        from_position = Position(7, 4)
        to_position = Position(5, 4)
        context = self.create_move_context(self.king, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_king_invalid_knight_move(self):
        from_position = Position(7, 4)
        to_position = Position(3, 2)
        context = self.create_move_context(self.king, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_king_capture(self):
        from_position = Position(7, 4)
        to_position = Position(6, 4)
        enemy_queen = Queen("Black", "Queen")
        self.board.set_position(to_position, enemy_queen)
        context = self.create_move_context(self.king, from_position, to_position)
        with self.assertRaises(KingisDeadException):
            self.chess.move(from_position.row, from_position.col, to_position.row, to_position.col)

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()