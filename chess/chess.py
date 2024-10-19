from chess.board import Board
from chess.exceptions import InvalidMoveError
from chess.movements import MovementRules
from chess.utils import MoveContext


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
        self.__ganador__ = None
    
    def is_within_board_limits(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move(self, from_row, from_col, to_row, to_col):
        # Obtiene la pieza a mover
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise InvalidMoveError("No hay ninguna pieza en esa posición.")
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise InvalidMoveError(f"Es el turno de {self.__turn__}, no de {piece.get_color()}.")
        # Crear el contexto del movimiento
        context = MoveContext(self.__board__, piece, from_row, from_col, to_row, to_col, self.__turn__)
        # Verificar si el movimiento es válido según las reglas de la pieza
        if not MovementRules.is_valid_move(context):
            raise InvalidMoveError("Movimiento no válido para la pieza seleccionada.")
        
        result = self.move_piece(from_row, from_col, to_row, to_col) # Realizar el movimiento y verificar si el rey fue capturado
        if result == "ReyEliminado":
            return "ReyEliminado"  # Enviar mensaje al main.py para finalizar el juego
        
        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()
        return "Valido"  # Movimiento realizado correctamente

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece:
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            self.__board__.set_position(from_row, from_col, None)
            print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")
        
        if self.__board__.get_piece(to_row, to_col).get_name() == "King":
            self.__ganador__ = self.__turn__
            return "ReyEliminado"
        
    def alternate_turn(self):
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__

    def display_board(self):
        self.__board__.display_board()

    def get_ganador(self):
        return self.__ganador__