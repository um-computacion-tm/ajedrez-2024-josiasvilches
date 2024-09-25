class Piece:
    def __init__(self, color, name, row, col):
        self.__color__ = color
        self.__name__ = name
        self.__row__ = row
        self.__col__ = col

    def __str__(self):
        if self.__color__ == "White":
            return self.white_str
        else:
            return self.black_str
        
    # method to obtain the actual position of the piece
    def get_position(self):
        return (self.__row__, self.__col__)

    # method to change the position of the piece
    def set_position(self, row, col):
        self.__row__ = row
        self.__col__ = col

    # method to obtain the color of the piece
    def get_color(self):
        return self.__color__
    
    # every piece has a different way to move, so its declared on its own file
    def possible_moves(self):
        pass

    def traverse_directions(self, directions):
        possible_moves = []
        for direction in directions:
            row, col = self.__row__, self.__col__

            while True:
                row += direction[0]
                col += direction[1]
                if 0 <= row < 7 and 0 <= col < 7:
                    possible_moves.append((row, col))
                else:
                    break

        return possible_moves
