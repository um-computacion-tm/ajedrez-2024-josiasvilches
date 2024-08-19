from pieces import Rook, Knight, Bishop

class Board:
    def __init__(self):
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        # Posiciones iniciales de los Rooks
        self.__positions__[0][0] = Rook("Black", 0, 0)
        self.__positions__[0][7] = Rook("Black", 0, 7)
        self.__positions__[7][7] = Rook("White", 7, 7)
        self.__positions__[7][0] = Rook("White", 7, 0)

        # Posiciones iniciales de los Knights
        self.__positions__[0][1] = Knight("Black", 0, 1)
        self.__positions__[0][6] = Knight("Black", 0, 6)
        self.__positions__[7][1] = Knight("White", 7, 1)
        self.__positions__[7][6] = Knight("White", 7, 6)

        # Posiciones iniciales de los Bishops
        self.__positions__[0][2] = Bishop("Black", 0, 2)
        self.__positions__[0][5] = Bishop("Black", 0, 5)
        self.__positions__[7][2] = Bishop("White", 7, 2)
        self.__positions__[7][5] = Bishop("White", 7, 5)

    def get_piece(self, row, col):
        return self.__positions__[row][col]
