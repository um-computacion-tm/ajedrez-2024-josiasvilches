import unittest
from chess.pawn import Pawn
from chess.board import Board
from chess.utils import *
from chess.movements import MovementRules
from chess.chess import Chess

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.chess = Chess()

    def test_pawn_single_step_forward(self):
        from_position = Position(6, 0)
        to_position = Position(5, 0)
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_pawn_double_step_forward(self):
        from_position = Position(6, 0)
        to_position = Position(4, 0)
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_pawn_capture_diagonal(self):
        from_position = Position(6, 0)
        to_position = Position(5, 1)
        self.board.set_position(to_position, Pawn("Black", "Pawn"))
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_pawn_invalid_move_backward(self):
        from_position = Position(6, 0)
        to_position = Position(7, 0)
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_pawn_invalid_move_horizontal(self):
        from_position = Position(6, 0)
        to_position = Position(6, 1)
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_pawn_invalid_move_diagonal_without_capture(self):
        from_position = Position(6, 0)
        to_position = Position(5, 1)
        pawn = self.board.get_piece(from_position)
        context = self.create_move_context(pawn, from_position, to_position)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, piece, from_position, to_position):
        game_context = GameContext(self.board, self.chess.get_turn())
        return MoveContext(game_context, piece, from_position, to_position)

if __name__ == '__main__':
    unittest.main()