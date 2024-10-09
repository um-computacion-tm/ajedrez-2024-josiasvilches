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

    def get_position(self):
        return (self.__row__, self.__col__)

    def set_position(self, row, col):
        self.__row__ = row
        self.__col__ = col

    def get_row(self):
        return self.__row__

    def get_col(self):
        return self.__col__
    
    def get_color(self):
        return self.__color__

    def possible_moves(self):
        pass

    def traverse_directions(self, directions):
        possible_moves = []
        for direction in directions:
            row, col = self.__row__, self.__col__

            while True:
                row += direction[0]
                col += direction[1]
                if 0 <= row < 8 and 0 <= col < 8:
                    possible_moves.append((row, col))
                else:
                    break

        return possible_moves
