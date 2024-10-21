import unittest
from chess.pieces import *
from chess.board import *
from chess.rook import Rook
from chess.utils import *
from chess.movements import MovementRules
from chess.exceptions import InvalidMoveError

class TestRook(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de pruebas."""
        self.rook = Rook('White', "Rook")  # Cambia el color según necesites
        self.board = MockBoard()  # Necesitarás implementar este mock
        self.from_position = Position(0, 0)  # Posición inicial
        self.to_position_horizontal = Position(0, 5)  # Movimiento horizontal válido
        self.to_position_vertical = Position(5, 0)  # Movimiento vertical válido
        self.to_position_invalid = Position(1, 1)  # Movimiento diagonal inválido
        
        self.board.set_piece(self.from_position, self.rook)  # Coloca la torre en el tablero

    def test_valid_horizontal_move(self):
        """Prueba un movimiento horizontal válido de la torre."""
        context = self.create_move_context(self.from_position, self.to_position_horizontal)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_valid_vertical_move(self):
        """Prueba un movimiento vertical válido de la torre."""
        context = self.create_move_context(self.from_position, self.to_position_vertical)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_invalid_diagonal_move(self):
        """Prueba un movimiento diagonal inválido de la torre."""
        context = self.create_move_context(self.from_position, self.to_position_invalid)
        self.assertFalse(MovementRules.is_valid_move(context))

    def test_path_clear(self):
        """Prueba que el camino esté despejado para un movimiento horizontal."""
        # Implementa aquí la lógica para verificar que el camino esté despejado
        self.board.set_piece(Position(0, 1), None)  # Elimina piezas en el camino
        context = self.create_move_context(self.from_position, self.to_position_horizontal)
        self.assertTrue(MovementRules.is_valid_move(context))

    def test_path_blocked(self):
        """Prueba que el movimiento sea inválido si hay una pieza en el camino."""
        blocking_piece = Rook('White', 'Rook')  # Pieza que bloquea el camino
        self.board.set_piece(Position(0, 3), blocking_piece)  # Coloca la pieza en el camino
        context = self.create_move_context(self.from_position, self.to_position_horizontal)
        self.assertFalse(MovementRules.is_valid_move(context))

    def create_move_context(self, from_pos, to_pos):
        """Crea un contexto de movimiento para las pruebas."""
        game_context = GameContext(self.board, "White")  # Ajusta el turno según sea necesario
        return MoveContext(game_context, self.rook, from_pos, to_pos)

# Aquí puedes agregar un mock para el tablero si no existe uno
class MockBoard:
    def __init__(self):
        self.pieces = {}  # Usar un diccionario para simular las piezas

    def set_piece(self, position, piece):
        self.pieces[(position.row, position.col)] = piece

    def get_piece(self, position):
        return self.pieces.get((position.row, position.col), None)

if __name__ == '__main__':
    unittest.main()
