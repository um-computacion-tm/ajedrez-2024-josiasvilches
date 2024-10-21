import unittest
from chess.chess import *
from chess.pieces import *
from chess.king import King
from chess.queen import Queen
from chess.bishop import Bishop
from chess.knight import Knight
from chess.rook import Rook
from chess.pawn import Pawn

class TestBoard(unittest.TestCase):
        
        def test_board_setup(self):
            self.board = Board()

        def test_get_piece_string(self):
            board = Board()
            
            # Test for King
            king = King("White", "King")
            self.assertEqual(board.get_piece_string(king), '♚ ')
            
            king = King("Black", "King")
            self.assertEqual(board.get_piece_string(king), '♔ ')
            
            # Test for Queen
            queen = Queen("White", "Queen")
            self.assertEqual(board.get_piece_string(queen), '♛ ')
            
            queen = Queen("Black", "Queen")
            self.assertEqual(board.get_piece_string(queen), '♕ ')
            
            # Test for Bishop
            bishop = Bishop("White", "Bishop")
            self.assertEqual(board.get_piece_string(bishop), '♝ ')
            
            bishop = Bishop("Black", "Bishop")
            self.assertEqual(board.get_piece_string(bishop), '♗ ')
            
            # Test for Knight
            knight = Knight("White", "Knight")
            self.assertEqual(board.get_piece_string(knight), '♞ ')
            
            knight = Knight("Black", "Knight")
            self.assertEqual(board.get_piece_string(knight), '♘ ')
            
            # Test for Rook
            rook = Rook("White", "Rook")
            self.assertEqual(board.get_piece_string(rook), '♜ ')
            
            rook = Rook("Black", "Rook")
            self.assertEqual(board.get_piece_string(rook), '♖ ')
            
            # Test for Pawn
            pawn = Pawn("White", "Pawn")
            self.assertEqual(board.get_piece_string(pawn), '♟ ')
            
            pawn = Pawn("Black", "Pawn")
            self.assertEqual(board.get_piece_string(pawn), '♙ ')
            
            # Test for None (empty space)
            self.assertEqual(board.get_piece_string(None), '. ')
    
if __name__ == '__main__':
    unittest.main()
