from chess.board import Board
from chess.exceptions import *
from chess.movements import MovementRules
from chess.utils import *


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
        self.white_pieces = 16  # Cantidad inicial de piezas blancas
        self.black_pieces = 16  # Cantidad inicial de piezas negras
        self.__ganador__ = None
    
    def is_within_board_limits(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move(self, from_row, from_col, to_row, to_col):
        from_position = Position(from_row, from_col)
        to_position = Position(to_row, to_col)

        # Obtiene la pieza a mover
        piece = self.__board__.get_piece(from_position)
        if piece is None:
            raise PieceNotFoundError()
        
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise NotYourTurnError()
        
        # Crear el contexto del movimiento
        game_context = GameContext(self.__board__, self.__turn__)
        context = MoveContext(game_context, piece, from_position, to_position)
        
        # Verificar si el movimiento es válido según las reglas de la pieza
        if not MovementRules.is_valid_move(context):
            raise InvalidMoveError()
        
        result = self.move_piece(from_position, to_position) # Realizar el movimiento y verificar si el rey fue capturado
        if result == "ReyEliminado":
            raise KingisDeadError()  # Enviar mensaje al main.py para finalizar el juego
        
        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()

    def move_piece(self, from_position, to_position):
        piece = self.__board__.get_piece(from_position)
        target_piece = self.__board__.get_piece(to_position)
        if piece:
            if target_piece:
                print(f"¡{piece.get_name()} en ({from_position.row}, {from_position.col}) capturó a {target_piece.get_name()} en ({to_position.row}, {to_position.col})!")

            self.__board__.move_piece(from_position, to_position)
            self.__board__.set_position(from_position, None)
            print(f"Tablero actualizado: {piece} movido a ({to_position.row}, {to_position.col})")
        
        if self.__board__.get_piece(to_position).get_name() == "King":
            self.__ganador__ = self.__turn__
            raise KingisDeadError()
    
    def count_pieces(self):
        """
        Cuenta las piezas blancas y negras en el tablero.
        """
        piece_counts = {"White": 0, "Black": 0}
        for row in self.__board__.__positions__:
            for piece in row:
                if piece is not None:
                    piece_counts[piece.get_color()] += 1
        
        self.white_pieces = piece_counts["White"]
        self.black_pieces = piece_counts["Black"]
        
        return self.white_pieces, self.black_pieces
        
    def alternate_turn(self):
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__

    def display_board(self):
        self.__board__.display_board()

    def get_ganador(self):
        return self.__ganador__