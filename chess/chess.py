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
        
        result = self.move_piece(from_row, from_col, to_row, to_col) # Realizar el movimiento y verificar si el rey fue capturado

        if result == "ReyEliminado":
            return "ReyEliminado"  # Enviar mensaje al main.py para finalizar el juego
        
        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()
        return "Valido"  # Movimiento realizado correctamente

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
        target_piece = self.__board__.get_piece(to_row, to_col)  # Verificar si hay una pieza en la posición destino
        if self.check_blocked_path(piece, from_row, from_col, to_row, to_col): # Verificar si el camino está bloqueado por una pieza aliada
            return "Movimiento bloqueado por una pieza aliada."
        
        if piece:
            self.__board__.set_position(to_row, to_col, piece)
            self.__board__.set_position(from_row, from_col, None)
            print(f"Tablero actualizado: {piece} movido a ({to_row}, {to_col})")

        if isinstance(target_piece, King): # Verificar si la pieza capturada es el rey
            self.__ganador__ = self.__turn__
            return "Rey capturado. ¡Fin del juego!"
        
        return "Movimiento válido"

    def check_blocked_path(self, piece, from_row, from_col, to_row, to_col):
        """Verifica si el camino está bloqueado por piezas aliadas."""
        if isinstance(piece, (Rook, Queen)):  # Movimiento en línea recta
            if from_row == to_row:
                return self.move_straight_line(from_row, from_col, to_row, to_col, "horizontal")
            elif from_col == to_col:
                return self.move_straight_line(from_row, from_col, to_row, to_col, "vertical")
        elif isinstance(piece, Bishop):  # Movimiento en diagonal
            return self.move_diagonal(from_row, from_col, to_row, to_col)
        elif isinstance(piece, Queen):  # Reina también se mueve en diagonal
            if from_row == to_row or from_col == to_col:
                return self.move_straight_line(from_row, from_col, to_row, to_col, "line")
            else:
                return self.move_diagonal(from_row, from_col, to_row, to_col)
        return False

    def move_straight_line(self, from_row, from_col, to_row, to_col, direction):
        """Mueve en línea recta (horizontal o vertical) y verifica el bloqueo."""
        if direction == "horizontal":
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.__board__.get_piece(from_row, col) is not None:
                    return True
        elif direction == "vertical":
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.__board__.get_piece(row, from_col) is not None:
                    return True
        return False

    def move_diagonal(self, from_row, from_col, to_row, to_col):
        """Mueve en diagonal y verifica el bloqueo."""
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if self.__board__.get_piece(row, col) is not None:
                return True
            row += row_step
            col += col_step
        return False

    def get_ganador(self):
        return self.__ganador__

    def alternate_turn(self):
        # Alternar turno entre "White" y "Black"
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_turn(self):
        return self.__turn__
    
    def display_board(self):
        self.__board__.display_board()
