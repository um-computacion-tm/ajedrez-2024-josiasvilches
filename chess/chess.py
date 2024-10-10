from chess.board import Board
from chess.exceptions import InvalidMoveError
from chess.movements import *
from chess.pieces import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"

    def move(self, from_row, from_col, to_row, to_col):
        # obtains the piece to move
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise InvalidMoveError("No hay ninguna pieza en esa posición.")
        
        # Verificar que la pieza sea del color correcto (según el turno)
        if piece.get_color() != self.__turn__:
            raise InvalidMoveError(f"Es el turno de {self.__turn__}, no de {piece.get_color()}.")
        
        # Verificar si el movimiento es válido según las reglas del tablero y la pieza
        if not self.__board__.is_valid_move(from_row, from_col, to_row, to_col):
            raise InvalidMoveError("Movimiento no válido para la pieza seleccionada.")
        
        # Realizar el movimiento
        movimiento_exitoso = self.__board__.move_piece(from_row, from_col, to_row, to_col)
        

        # if the movement is valid there's a change in the turn
        self.change_turn()
    
    def change_turn(self):
        # changes the turn between white and black
        
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"

    def get_turn(self):
        # show actual turn
        return self.__turn__
    
    def display_board(self):
        # show the board
        self.__board__.display_board()

