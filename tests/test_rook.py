import unittest
from chess.rook import *

class TestRook(unittest.TestCase):
    def test_str(self):
        rook = Rook("White", 0, 0)
        self.assertEqual(str(rook), "♜")

    def test_move_vertical_desc(self):
        rook = Rook("White", 0, 0)
        possibles = rook.posible_positions(4, 0)
        self.assertEqual(possibles, [(5,0), (6,0), (7,0)])