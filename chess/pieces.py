class Piece:
    def __init__(self, color, nombre, fila, columna):
        self.__color__ = color
        self.__nombre__ = nombre
        self.__fila__ = fila
        self.__columna__ = columna
        
    # Getters y Setters de los atributos
    def get_position(self):
        return (self.__fila__, self.__columna__)

    def set_position(self, fila, columna):
        self.__fila__ = fila
        self.__columna__ = columna

    def get_color(self):
        return self.__color__

    def get_nombre(self):
        return self.__nombre__

class Rook(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Rook', fila, columna)


class Knight(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Knight', fila, columna)

class Bishop(Piece):
    def __init__(self, color, fila=None, columna=None):
        super().__init__(color, 'Bishop', fila, columna)