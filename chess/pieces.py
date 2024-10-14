class Piece:
    def __init__(self, color, row, col):
        self.__color__ = color
        self.__row__ = row
        self.__col__ = col

    def __str__(self):
        if self.__color__ == "White":
            return self.__white_str__
        else:
            return self.__black_str__

    # obtains position of the piece
    def get_position(self):
        return (self.__row__, self.__col__)

    # changes the position of the piece
    def set_position(self, row, col):
        self.__row__ = row
        self.__col__ = col

    # obtains the color of the piece
    def get_color(self):
        return self.__color__

    def possible_moves(self, board):
        return MovementRules.get_possible_moves(self, board)
