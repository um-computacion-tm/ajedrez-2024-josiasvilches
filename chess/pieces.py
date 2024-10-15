class Piece:
    def __init__(self, color, name):
        self.__color__ = color
        self.__name__ = name

    def __str__(self):
        if self.__color__ == "White":
            return self.__white_str__
        else:
            return self.__black_str__
        
    # obtains the color of the piece
    def get_color(self):
        return self.__color__

    # obtains the name of the piece
    def get_name(self):
        return self.__name__
