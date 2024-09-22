class Piece:
    def __init__(self, color, name, fila, columna):
        self.__color__ = color
        self.__name__ = name
        self.__fila__ = fila
        self.__columna__ = columna
        
    # method to obtain the actual position of the piece
    def get_position(self):
        return (self.__fila__, self.__columna__)

    # method to change the position of the piece
    def set_position(self, fila, columna):
        self.__fila__ = fila
        self.__columna__ = columna

    # method to obtain the color of the piece
    def get_color(self):
        return self.__color__
    
    # every piece has a different way to move, so its declared on its own file
    def possible_moves(self):
        pass

    def traverse_directions(self, directions):
        possible_moves = []
        for direction in directions:
            fila, columna = self.__fila__, self.__columna__

            while True:
                fila += direction[0]
                columna += direction[1]
                if 0 <= fila < 7 and 0 <= columna < 7:
                    possible_moves.append((fila, columna))
                else:
                    break

        return possible_moves
