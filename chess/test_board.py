import unittest
from board import Board
from pieces import *

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
    
    def test_initial_rook_positions(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color(), "White")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).get_color(), "White")
    
    def test_initial_knight_positions(self):
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertEqual(self.board.get_piece(0, 1).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertEqual(self.board.get_piece(0, 6).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertEqual(self.board.get_piece(7, 1).get_color(), "White")
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertEqual(self.board.get_piece(7, 6).get_color(), "White")
    
    def test_initial_bishop_positions(self):
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.board.get_piece(0, 2).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertEqual(self.board.get_piece(0, 5).get_color(), "Black")
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertEqual(self.board.get_piece(7, 2).get_color(), "White")
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertEqual(self.board.get_piece(7, 5).get_color(), "White")

if __name__ == '__main__':
    unittest.main()
