import unittest
from chess.rook import Rook
from chess.board import Board
from chess.utils import Position, GameContext, MoveContext
from chess.movements import MovementRules
from chess.chess import Chess

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()
        self.rook = Rook("White", "Rook")
        self.board.set_position(Position(7, 0), self.rook)

    # def test_rook_horizontal_move(self):
    #     from_position = Position(7, 0)
    #     to_position = Position(7, 5)
    #     context = self.create_move_context(self.rook, from_position, to_position)
    #     self.assertTrue(MovementRules.is_valid_move(context))

    # def test_rook_vertical_move(self):
    #     from_position = Position(7, 0)
    #     to_position = Position(4, 0)
    #     context = self.create_move_context(self.rook, from_position, to_position)
    #     self.assertTrue(MovementRules.is_valid_move(context))

    def test_rook_invalid_diagonal_move(self):
        from_position = Position(7, 0)
        to_position = Position(5, 2)
        context = self.create_move_context(self.rook, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_rook_invalid_knight_move(self):
        from_position = Position(7, 0)
        to_position = Position(5, 1)
        context = self.create_move_context(self.rook, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()