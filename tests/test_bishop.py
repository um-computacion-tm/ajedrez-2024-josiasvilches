import unittest
from chess.bishop import Bishop
from chess.pieces import *
from chess.board import Board

class TestBishop(unittest.TestCase):
    def test_str(self):
        bishop = Bishop("White", 0, 2)
        self.assertEqual(str(bishop), "♝")

    def test_move_diagonal(self):
        bishop = Bishop("White", 0, 2)
        possibles = bishop.posible_positions(4, 6)
        self.assertEqual(possibles, [(1, 3), (2, 4), (3, 5), (5, 7)])

    def test_move_diagonal_blocked(self):
        bishop = Bishop("White", 0, 2)
        # Assuming the board has a piece at (2, 4)
        board = {(2, 4): 'Piece'}
        possibles = bishop.posible_positions(4, 6, board)
        self.assertEqual(possibles, [(1, 3)])

if __name__ == '__main__':
    unittest.main()