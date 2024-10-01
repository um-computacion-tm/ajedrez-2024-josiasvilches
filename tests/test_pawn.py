import unittest
from chess.pawn import Pawn

class MockBoard:
    """ Clase Mock para representar un tablero de ajedrez simplificado para los tests """
    def __init__(self):
        # Un tablero vacío
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def get_board(self):
        return self.board


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = MockBoard().get_board()
        # Peones
        self.white_pawn = Pawn('White', 6, 0)  # Inicialmente en la fila 6, columna 0
        self.black_pawn = Pawn('Black', 1, 0)  # Inicialmente en la fila 1, columna 0
        self.board[6][0] = self.white_pawn
        self.board[1][0] = self.black_pawn

    def test_pawn_initial_double_move_white(self):
        """ Test para verificar que el peón blanco puede avanzar dos pasos desde su posición inicial """
        self.assertTrue(self.white_pawn.is_valid_move(4, 0, self.board))

    def test_pawn_initial_double_move_black(self):
        """ Test para verificar que el peón negro puede avanzar dos pasos desde su posición inicial """
        self.assertTrue(self.black_pawn.is_valid_move(3, 0, self.board))

    def test_pawn_single_move_white(self):
        """ Test para verificar que el peón blanco puede avanzar un paso """
        self.assertTrue(self.white_pawn.is_valid_move(5, 0, self.board))

    def test_pawn_single_move_black(self):
        """ Test para verificar que el peón negro puede avanzar un paso """
        self.assertTrue(self.black_pawn.is_valid_move(2, 0, self.board))

    def test_pawn_move_blocked(self):
        """ Test para verificar que el peón no puede moverse hacia una casilla ocupada """
        blocking_pawn = Pawn('White', 5, 0)
        self.board[5][0] = blocking_pawn
        self.assertFalse(self.white_pawn.is_valid_move(5, 0, self.board))

    def test_pawn_capture_diagonal_white(self):
        """ Test para verificar que el peón blanco puede capturar en diagonal """
        black_pawn = Pawn('Black', 5, 1)
        self.board[5][1] = black_pawn
        self.assertTrue(self.white_pawn.is_valid_move(5, 1, self.board))

    def test_pawn_capture_diagonal_black(self):
        """ Test para verificar que el peón negro puede capturar en diagonal """
        white_pawn = Pawn('White', 2, 1)
        self.board[2][1] = white_pawn
        self.assertTrue(self.black_pawn.is_valid_move(2, 1, self.board))

    def test_pawn_invalid_move(self):
        """ Test para verificar que un movimiento inválido del peón es rechazado """
        self.assertFalse(self.white_pawn.is_valid_move(6, 1, self.board))  # Movimiento lateral inválido

    def test_pawn_invalid_double_move_after_first(self):
        """ Test para verificar que el peón no puede moverse dos casillas después de haberse movido """
        self.white_pawn.move(5, 0)  # Mover peón blanco hacia adelante una casilla
        self.assertFalse(self.white_pawn.is_valid_move(3, 0, self.board))

if __name__ == '__main__':
    unittest.main()
