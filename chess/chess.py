from chess.board import Board
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"

    def move(
            self, 
            from_row, 
            from_col, 
            to_row, 
            to_col):
        ...

        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"