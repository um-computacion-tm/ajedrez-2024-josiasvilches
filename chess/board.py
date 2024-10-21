from chess.king import *
from chess.queen import *
from chess.bishop import *
from chess.rook import *
from chess.knight import *
from chess.pawn import *

class Board:
    def __init__(self):
        '''
        The constructor initializes the board with an 8x8 grid of None values and sets the turn to "White".
        '''
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__turn__ = "White"
        # Posiciones iniciales de los Rooks
        self.__positions__[0][0] = Rook("Black", "Rook")
        self.__positions__[0][7] = Rook("Black", "Rook")
        self.__positions__[7][7] = Rook("White", "Rook")
        self.__positions__[7][0] = Rook("White", "Rook")

        # Posiciones iniciales de los Knights
        self.__positions__[0][1] = Knight("Black", "Knight")
        self.__positions__[0][6] = Knight("Black", "Knight")
        self.__positions__[7][1] = Knight("White", "Knight")
        self.__positions__[7][6] = Knight("White", "Knight")

        # Posiciones iniciales de los Bishops
        self.__positions__[0][2] = Bishop("Black", "Bishop")
        self.__positions__[0][5] = Bishop("Black", "Bishop")
        self.__positions__[7][2] = Bishop("White", "Bishop")
        self.__positions__[7][5] = Bishop("White", "Bishop")

        # Posiciones iniciales de la reina
        self.__positions__[0][3] = Queen("Black", "Queen")
        self.__positions__[7][3] = Queen("White", "Queen")

        # Posiciones iniciales del rey
        self.__positions__[0][4] = King("Black", "King")
        self.__positions__[7][4] = King("White", "King")

        # Posiciones iniciales de los peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("Black", "Pawn")
            self.__positions__[6][i] = Pawn("White", "Pawn")
    
    def get_piece(self, position):
        '''
        The function get_piece() returns the piece at the given position on the board.
        Parameters:
            position: The position on the board.
        Returns:
            The piece at the given position.
        '''
        return self.__positions__[position.row][position.col]
    
    def move_piece(self, from_position, to_position):
        '''
        The function move_piece() moves a piece from one position to another on the board.
        Parameters:
            from_position: The starting position of the piece.
            to_position: The destination position of the piece.
        '''
        piece = self.get_piece(from_position)
        self.__positions__[to_position.row][to_position.col] = piece
        self.__positions__[from_position.row][from_position.col] = None

    def set_position(self, position, piece):
        '''
        The function set_position() sets a piece at the given position on the board.
        Parameters:
            position: The position on the board.
            piece: The piece to be placed at the given position.
        '''
        self.__positions__[position.row][position.col] = piece

    def get_turn(self):
        '''
        The function get_turn() returns the current turn.
        Returns:
            The current turn ("White" or "Black").
        '''
        return self.__turn__

    def display_board(self):
        '''
        The function display_board() displays the board with column labels, a dividing line, and the rows of the board.
        '''
        self.print_column_labels()
        self.print_line()
        self.print_board_rows()
        self.print_line()
        self.print_column_labels()

    def print_column_labels(self):
        '''
        The function print_column_labels() prints the column labels (a-h).
        '''
        print("  a b c d e f g h")  # Etiquetas de columnas
    
    def print_line(self):
        '''
        The function print_line() prints a dividing line.
        '''
        print(" +-----------------+")  # Línea divisoria

    def print_board_rows(self):
        '''
        The function print_board_rows() prints each row of the board.
        '''
        for row in range(8):
            row_str = self.get_row_string(row)
            print(row_str)

    def get_row_string(self, row):
        '''
        The function get_row_string() returns a string representation of a row on the board.
        Parameters:
            row: The row number.
        Returns:
            A string representation of the row.
        '''
        row_str = f"{0 + row}|"  # Etiquetas de filas
        for col in range(8):
            piece = self.__positions__[row][col]
            row_str += self.get_piece_string(piece)
        row_str += f"|{0 + row}"
        return row_str

    def get_piece_string(self, piece):
        '''
        The function get_piece_string() returns a string representation of a piece.
        Parameters:
            piece: The piece to be represented.
        Returns:
            A string representation of the piece.
        '''
        if piece is None:
            return ". "  # Espacio vacío
        else:
            return str(piece) + " "