class ChessError(Exception):
    """Base class for other chess-related exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidMoveError(ChessError):
    """Raised when a move is invalid"""
    def __init__(self, message="Realizaste un movimiento inválido"):
        super().__init__(message)

class PieceNotFoundError(ChessError):
    """Raised when a piece is not found on the board"""
    def __init__(self, message="La pieza seleccionada no fue encontrada en el tablero"):
        super().__init__(message)

class GameOverException(ChessError):
    """Raised when a team wins the game"""
    def __init__(self, message="Juego terminado"):
        super().__init__(message)

class InvalidInputError(ChessError):
    """Raised when the input is invalid"""
    def __init__(self, message="Por favor ingresa números enteros para las filas y letras para las columnas."):
        super().__init__(message)

class NotYourTurnError(ChessError):
    """Raised when a player tries to move a piece that is not theirs"""
    def __init__(self, message="No es tu turno"):
        super().__init__(message)

class KingisDeadException(ChessError):
    """Raised when the king is captured"""
    def __init__(self, message="El rey ha sido capturado"):
        super().__init__(message)

class OutOfBoundsError(ChessError):
    """Raised when a piece is moved out of the board"""
    def __init__(self, message="Las coordenadas ingresadas están fuera de los límites del tablero"):
        super().__init__(message)