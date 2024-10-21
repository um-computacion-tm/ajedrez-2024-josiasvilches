from chess.board import Board
from chess.exceptions import *
from chess.movements import MovementRules
from chess.utils import *

class Chess:
    def __init__(self):
        '''
        The constructor initializes the chess game with a board, sets the turn to "White",
        and initializes the piece counts for both white and black pieces.
        '''
        self.__board__ = Board()
        self.__turn__ = "White"
        self.white_pieces = 16  # Cantidad inicial de piezas blancas
        self.black_pieces = 16  # Cantidad inicial de piezas negras
        self.__ganador__ = None  # Ganador del juego (None al inicio)
    
    def is_within_board_limits(self, row, col):
        '''
        The function is_within_board_limits() checks if the given row and column are within the board limits.
        Parameters:
            row: The row index.
            col: The column index.
        Returns:
            True if the row and column are within the board limits.
        Raises:
            OutOfBoundsError: If the row or column is out of the board limits.
        '''
        if not (0 <= row < 8 and 0 <= col < 8):
            raise OutOfBoundsError()
        return True

    def move(self, from_row, from_col, to_row, to_col):
        '''
        The function move() moves a piece from one position to another on the board.
        Parameters:
            from_row: The starting row index.
            from_col: The starting column index.
            to_row: The destination row index.
            to_col: The destination column index.
        '''
        # Verificar que las coordenadas estén dentro de los límites del tablero
        self.is_within_board_limits(from_row, from_col)
        self.is_within_board_limits(to_row, to_col)
        
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
            raise KingisDeadException()  
        
        # Cambiar el turno si el movimiento es exitoso
        self.alternate_turn()

    def move_piece(self, from_position, to_position):
        '''
        The function move_piece() moves a piece from one position to another on the board.
        Parameters:
            from_position: The starting position of the piece.
            to_position: The destination position of the piece.
        '''
        piece = self.__board__.get_piece(from_position)
        target_piece = self.__board__.get_piece(to_position)
        
        self.capture_piece(piece, target_piece, from_position, to_position)
        self.__board__.move_piece(from_position, to_position)
        self.__board__.set_position(from_position, None)
        print(f"Tablero actualizado: {piece} movido a ({to_position.row}, {to_position.col})")
        
        self.check_king_captured(to_position)

    def capture_piece(self, piece, target_piece, from_position, to_position):
        '''
        The function capture_piece() handles the logic for capturing a piece.
        Parameters:
            piece: The piece to be moved.
            target_piece: The piece to be captured.
            from_position: The starting position of the piece.
            to_position: The destination position of the piece.
        '''
        if piece and target_piece:
            print(f"¡{piece} en ({from_position.row}, {from_position.col}) capturó a {target_piece} en ({to_position.row}, {to_position.col})!")

    def check_king_captured(self, to_position):
        '''
        The function check_king_captured() checks if the king has been captured.
        Parameters:
            to_position: The position to which the piece was moved.
        Raises:
            KingisDeadException: If the king has been captured.
        '''
        if self.__board__.get_piece(to_position).get_name() == "King":
            self.__ganador__ = self.__turn__
            raise KingisDeadException()

    def display_board(self):
        '''
        The function display_board() displays the current state of the board.
        '''
        self.__board__.display_board()

    def get_turn(self):
        '''
        The function get_turn() returns the current turn.
        Returns:
            The current turn ("White" or "Black").
        '''
        return self.__turn__

    def count_pieces(self):
        '''
        The function count_pieces() counts the number of pieces for each color.
        Returns:
            A tuple containing the number of white pieces and black pieces.
        '''
        piece_counts = self.initialize_piece_counts()
        self.update_piece_counts(piece_counts)
        self.white_pieces = piece_counts["White"]
        self.black_pieces = piece_counts["Black"]
        return self.white_pieces, self.black_pieces

    def initialize_piece_counts(self):
        '''
        The function initialize_piece_counts() initializes the piece counts for both colors.
        Returns:
            A dictionary with the initial piece counts for both colors.
        '''
        return {"White": 0, "Black": 0}

    def update_piece_counts(self, piece_counts):
        '''
        The function update_piece_counts() updates the piece counts based on the current state of the board.
        Parameters:
            piece_counts: A dictionary with the current piece counts for both colors.
        '''
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(Position(row, col))
                if piece is not None:
                    piece_counts[piece.get_color()] += 1

    def alternate_turn(self):
        '''
        The function alternate_turn() switches the turn to the other player.
        '''
        self.__turn__ = "White" if self.__turn__ == "Black" else "Black"
        print(f"Es el turno de {self.__turn__}")

    def get_ganador(self):
        '''
        The function get_ganador() returns the winner of the game.
        Returns:
            The winner of the game.
        '''
        return self.__ganador__