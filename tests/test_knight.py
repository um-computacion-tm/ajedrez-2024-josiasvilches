import unittest
from chess.knight import Knight
from chess.board import Board
from chess.utils import Position, GameContext, MoveContext
from chess.movements import MovementRules
from chess.chess import Chess

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()
        self.knight = Knight("White", "Knight")
        self.board.set_position(Position(7, 1), self.knight)

    def test_knight_L_move(self):
        from_position = Position(7, 1)
        to_position = Position(5, 2)
        context = self.create_move_context(self.knight, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_knight_invalid_horizontal_move(self):
        from_position = Position(7, 1)
        to_position = Position(7, 3)
        context = self.create_move_context(self.knight, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_knight_invalid_vertical_move(self):
        from_position = Position(7, 1)
        to_position = Position(5, 1)
        context = self.create_move_context(self.knight, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_knight_invalid_diagonal_move(self):
        from_position = Position(7, 1)
        to_position = Position(5, 3)
        context = self.create_move_context(self.knight, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()