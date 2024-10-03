class MovementRules:
    # Rook

    def get_possible_moves(self, from_row, from_col):
        possibles = []
        for to_row in range(from_row + 1, 8):
            possibles.append((to_row, from_col))
        for to_row in range(from_row - 1, -1, -1):
            possibles.append((to_row, from_col))

        # Movimiento horizontal hacia izquierda y derecha
        for to_col in range(from_col + 1, 8):
            possibles.append((from_row, to_col))
        for to_col in range(from_col - 1, -1, -1):
            possibles.append((from_row, to_col))

        return possibles
    
    # Bishop
    def is_valid(self, row, col):
        if abs(self.row - row) == abs(self.col - col):
            return True
        return False
    
    def move(self, row, col):
        if self.is_valid(row, col):
            self.row = row
            self.col = col
            return True
        return False
    def posible_positions(self, row, col):
        possibles = []
        for i in range(1, 8):
            if 0 <= row + i < 8 and 0 <= col + i < 8:
                possibles.append((row + i, col + i))
            if 0 <= row - i < 8 and 0 <= col + i < 8:
                possibles.append((row - i, col + i))
            if 0 <= row + i < 8 and 0 <= col - i < 8:
                possibles.append((row + i, col - i))
            if 0 <= row - i < 8 and 0 <= col - i < 8:
                possibles.append((row - i, col - i))
        return possibles

    # Pawn

    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.get_position()
        direction = 1 if self.get_color() == 'White' else -1

        # Movimiento estándar de un paso hacia adelante
        if from_col == to_col:
            # verifies that the destination square is empty
            if board[to_row][to_col] is None:
                # one step forward
                if (to_row - from_row) == direction:
                    return True
            # Movimiento inicial de dos pasos hacia adelante
                if not self.__has_moved__ and (to_row - from_row) == 2 * direction:
                    if board[from_row + direction][from_col] is None:
                        return True
        
        # Movimiento de captura diagonal
        if abs(from_col - to_col) == 1 and (to_row - from_row) == direction:
            if board[to_row][to_col] is not None and board[to_row][to_col].get_color() != self.get_color():
                return True
    

        return False
    
    def get_possible_moves(self, from_row, from_col):
        possible_moves = []
        if self.get_color() == "White":
            # Movimiento normal hacia adelante
            if self.get_row() > 0:
                possible_moves.append((from_row - 1, from_col))
            # Movimiento de doble casilla desde la posición inicial
            if from_row == 6 and self.get_row() > 1:
                possible_moves.append((from_row - 2, from_col))
        else:
            # Movimiento normal hacia adelante para las negras
            if self.get_row() < 7:
                possible_moves.append((from_row + 1, from_col))
            # Movimiento de doble casilla desde la posición inicial
            if from_row == 1 and self.get_row() < 6:
                possible_moves.append((from_row + 2, from_col))

        return possible_moves

    def move(self, to_row, to_col):
        self.__has_moved__ = True
        self.set_position(to_row, to_col)

    # Queen

    def get_moves(self, board):
        moves = []
        for i in range(1, 8):
            if self.row + i < 8:
                if board[self.row + i][self.col] == None:
                    moves.append((self.row + i, self.col))
                elif board[self.row + i][self.col].color != self.color:
                    moves.append((self.row + i, self.col))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if self.row - i >= 0:
                if board[self.row - i][self.col] == None:
                    moves.append((self.row - i, self.col))
                elif board[self.row - i][self.col].color != self.color:
                    moves.append((self.row - i, self.col))
                    break
                else:
                    break
            else:
                break
    
    # King

    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.get_position()
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True
        return False
    def move(self, to_row, to_col):
        self.set_position(to_row, to_col)
        return True    
    
    # Knight

    def is_valid_move(self, row, col, board):
        # L movement
        if (abs(from_row - row) == 2 and abs(from_col - col) == 1) or (abs(from_row - row) == 1 and abs(from_col - col) == 2):
            return True
        return False
    
    def move(self, row, col):
        if self.is_valid(row, col):
            self.row = row
            self.col = col
            return True
        return False
    