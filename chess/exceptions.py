class ChessError(Exception):
    """Base class for other chess-related exceptions"""
    pass

class InvalidMoveError(ChessError):
    """Raised when a move is invalid"""
    def __init__(self, message="Realizaste un movimiento inválido"):
        self.message = message
        super().__init__(self.message)

class PieceNotFoundError(ChessError):
    """Raised when a piece is not found on the board"""
    def __init__(self, message="La pieza no fue encontrada en el tablero"):
        self.message = message
        super().__init__(self.message)