import unittest
from chess.bishop import Bishop
from chess.board import Board
from chess.utils import Position, GameContext, MoveContext
from chess.movements import MovementRules
from chess.chess import Chess

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()
        self.bishop = Bishop("White", "Bishop")
        self.board.set_position(Position(7, 2), self.bishop)

    def test_bishop_diagonal_move(self):
        from_position = Position(7, 2)
        to_position = Position(5, 4)
        context = self.create_move_context(self.bishop, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_bishop_invalid_horizontal_move(self):
        from_position = Position(7, 2)
        to_position = Position(7, 5)
        context = self.create_move_context(self.bishop, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_bishop_invalid_vertical_move(self):
        from_position = Position(7, 2)
        to_position = Position(4, 2)
        context = self.create_move_context(self.bishop, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_bishop_invalid_knight_move(self):
        from_position = Position(7, 2)
        to_position = Position(5, 3)
        context = self.create_move_context(self.bishop, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()