import unittest
from unittest.mock import patch
from chess.cli import get_user_input, convert_input_to_indices, check_game_over, handle_user_move, play
from chess.chess import Chess
from chess.utils import *
from chess.exceptions import InvalidInputError, GameOverException, KingisDeadException

class TestCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', 'a', '1', 'b'])
    def test_get_user_input_valid(self, mock_input):
        from_row, from_col, to_row, to_col = get_user_input()
        self.assertEqual((from_row, from_col, to_row, to_col), ('0', 'a', '1', 'b'))

    @patch('builtins.input', side_effect=['salir'])
    def test_get_user_input_exit(self, mock_input):
        from_row, from_col, to_row, to_col = get_user_input()
        self.assertEqual((from_row, from_col, to_row, to_col), (None, None, None, None))

    def test_convert_input_to_indices_valid(self):
        from_row, from_col, to_row, to_col = convert_input_to_indices('0', 'a', '1', 'b')
        self.assertEqual((from_row, from_col, to_row, to_col), (0, 0, 1, 1))

    def test_convert_input_to_indices_invalid(self):
        with self.assertRaises(InvalidInputError):
            convert_input_to_indices('x', 'a', '1', 'b')

    def test_check_game_over_white_wins(self):
        chess = Chess()
        # Eliminar todas las piezas negras
        for row in range(8):
            for col in range(8):
                piece = chess.__board__.get_piece(Position(row, col))
                if piece and piece.get_color() == "Black":
                    chess.__board__.set_position(Position(row, col), None)
        with self.assertRaises(GameOverException):
            chess.check_game_over()


    def test_check_game_over_black_wins(self):
        chess = Chess()
        # Eliminar todas las piezas blancas
        for row in range(8):
            for col in range(8):
                piece = chess.__board__.get_piece(Position(row, col))
                if piece and piece.get_color() == "White":
                    chess.__board__.set_position(Position(row, col), None)
        with self.assertRaises(GameOverException):
            chess.check_game_over()


    @patch('chess.cli.get_user_input', return_value=('0', 'a', '1', 'b'))
    @patch('chess.cli.convert_input_to_indices', return_value=(0, 0, 1, 1))
    @patch('chess.chess.Chess.move')
    @patch('chess.cli.check_game_over')
    def test_handle_user_move_valid(self, mock_check_game_over, mock_move, mock_convert, mock_input):
        chess = Chess()
        result = handle_user_move(chess)
        self.assertTrue(result)
        mock_move.assert_called_once_with(0, 0, 1, 1)
        mock_check_game_over.assert_called_once_with(chess)

    @patch('chess.cli.get_user_input', return_value=(None, None, None, None))
    def test_handle_user_move_exit(self, mock_input):
        chess = Chess()
        result = handle_user_move(chess)
        self.assertFalse(result)

    @patch('chess.cli.handle_user_move', return_value=False)
    @patch('chess.chess.Chess.display_board')
    @patch('chess.chess.Chess.get_turn', return_value='White')
    def test_play(self, mock_get_turn, mock_display_board, mock_handle_user_move):
        chess = Chess()
        play(chess)
        mock_display_board.assert_called()
        mock_get_turn.assert_called()
        mock_handle_user_move.assert_called()

if __name__ == '__main__':
    unittest.main()