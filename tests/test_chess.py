import unittest
from chess.chess import Chess
from chess.utils import Position
from chess.exceptions import PieceNotFoundError, NotYourTurnError, InvalidMoveError, OutOfBoundsError, KingisDeadException
from chess.king import King
from chess.pawn import Pawn
from chess.queen import Queen

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_valid_move(self):
        # Movimiento válido de un peón blanco
        self.chess.move(6, 0, 5, 0)
        piece = self.chess.get_board().get_piece(Position(5, 0))
        self.assertIsNotNone(piece)
        self.assertEqual(piece.get_name(), "Pawn")
        self.assertEqual(piece.get_color(), "White")

    def test_invalid_move(self):
        # Movimiento inválido de un peón blanco (movimiento horizontal)
        with self.assertRaises(InvalidMoveError):
            self.chess.move(6, 0, 6, 1)

    def test_move_out_of_bounds(self):
        # Movimiento fuera de los límites del tablero
        with self.assertRaises(OutOfBoundsError):
            self.chess.move(6, 0, 8, 0)

    def test_capture_piece(self):
        # Captura de un peón negro por un peón blanco
        self.chess.move(6, 0, 4, 0)  # Mover peón blanco dos pasos adelante
        self.chess.move(1, 1, 3, 1)  # Mover peón negro dos pasos adelante
        self.chess.move(4, 0, 3, 1)  # Capturar peón negro
        piece = self.chess.get_board().get_piece(Position(3, 1))
        self.assertIsNotNone(piece)
        self.assertEqual(piece.get_name(), "Pawn")
        self.assertEqual(piece.get_color(), "White")

    def test_turn_change(self):
        # Verificar que el turno cambia después de un movimiento válido
        self.assertEqual(self.chess.get_turn(), "White")
        self.chess.move(6, 0, 5, 0)
        self.assertEqual(self.chess.get_turn(), "Black")

if __name__ == '__main__':
    unittest.main()