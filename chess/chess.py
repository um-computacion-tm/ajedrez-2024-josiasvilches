from chess.board import *
from chess.exceptions import InvalidMoveError
from chess.pieces import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"

    def move(self, from_row, from_col, to_row, to_col):
        # Obtiene la pieza a mover
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise InvalidMoveError("No hay ninguna pieza en esa posición.")
        
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise InvalidMoveError(f"Es el turno de {self.__turn__}, no de {piece.get_color()}.")
        
        # Verificar si el movimiento es válido según las reglas de la pieza
        if not self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            raise InvalidMoveError("Movimiento no válido para la pieza seleccionada.")
        
        # Realizar el movimiento
        self.move_piece(from_row, from_col, to_row, to_col)

        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()

    def is_valid_move(self, piece, from_row, from_col, to_row, to_col):
        # Verificar que las coordenadas estén dentro de los límites del tablero
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            return False
        
        # Obtener la pieza de destino
        destination_piece = self.__board__.get_piece(to_row, to_col)
        
        # Verificar si la casilla de destino está vacía o tiene una pieza enemiga
        if destination_piece is not None and destination_piece.get_color() == piece.get_color():
            return False  # Movimiento no válido si es una pieza aliada

        # Validar los movimientos dependiendo del tipo de pieza
        piece_type = type(piece).__name__

        if piece_type == "Rook":
            return self.is_valid_rook_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Bishop":
            return self.is_valid_bishop_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Knight":
            return self.is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Queen":
            return self.is_valid_queen_move(from_row, from_col, to_row, to_col)
        elif piece_type == "King":
            return self.is_valid_king_move(from_row, from_col, to_row, to_col)
        elif piece_type == "Pawn":
            return self.is_valid_pawn_move(piece, from_row, from_col, to_row, to_col)

        return False  # Si no se reconoce la pieza, el movimiento es inválido

    # Regla de movimiento para la torre (Rook)
    def is_valid_rook_move(self, from_row, from_col, to_row, to_col):
        return (from_row == to_row or from_col == to_col)

    # Regla de movimiento para el alfil (Bishop)
    def is_valid_bishop_move(self, from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)

    # Regla de movimiento para el caballo (Knight)
    def is_valid_knight_move(self, from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    # Regla de movimiento para la reina (Queen)
    def is_valid_queen_move(self, from_row, from_col, to_row, to_col):
        return self.is_valid_rook_move(from_row, from_col, to_row, to_col) or self.is_valid_bishop_move(from_row, from_col, to_row, to_col)

    # Regla de movimiento para el rey (King)
    def is_valid_king_move(self, from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1

    # Regla de movimiento para el peón (Pawn)
    def is_valid_pawn_move(self, pawn, from_row, from_col, to_row, to_col):
        direction = -1 if pawn.get_color() == "White" else 1
        # Movimiento hacia adelante
        if from_col == to_col:
            if to_row == from_row + direction and self.__board__.get_piece(to_row, to_col) is None:
                return True
            # Movimiento inicial doble
            if (from_row == 6 and direction == -1) or (from_row == 1 and direction == 1):
                if to_row == from_row + 2 * direction and self.__board__.get_piece(to_row, to_col) is None:
                    return True
        # Captura diagonal
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            return self.__board__.get_piece(to_row, to_col) is not None

        return False  # Cualquier otro movimiento es inválido para el peón

    def move_piece(self, from_row, from_col, to_row, to_col):
        # Mueve la pieza y actualiza la posición en el tablero
        piece = self.__board__.get_piece(from_row, from_col)
        if piece:
            self.__board__.set_piece(to_row, to_col, piece)
            self.__board__.set_piece(from_row, from_col, None)
            piece.set_position(to_row, to_col)

            print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")

    def alternate_turn(self):
        # Alternar turno entre "White" y "Black"
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__
    
    def display_board(self):
        self.__board__.display_board()
