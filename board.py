from pieces import *
class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.__positions__[0][0] = Rook("Black")
        self.__positions__[0][7] = Rook("Black")
        self.__positions__[7][7] = Rook("White")
        self.__positions__[7][0] = Rook("White")
        self.__positions__[0][1] = Horse("Black")
        self.__positions__[0][6] = Horse("Black")
        self.__positions__[7][1] = Horse("White")
        self.__positions__[7][6] = Horse("White")
        self.__positions__[0][2] = Bishop("Black")
        self.__positions__[0][5] = Bishop("Black")
        self.__positions__[7][2] = Bishop("White")
        self.__positions__[7][5] = Bishop("White")
    
    