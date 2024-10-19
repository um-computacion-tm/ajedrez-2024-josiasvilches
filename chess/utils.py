class MoveContext:
    def __init__(self, board, piece, from_row, from_col, to_row, to_col, turn):
        self.board = board
        self.piece = piece
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col
        self.turn = turn

def is_path_clear_linear(board, from_fixed, from_var, to_var, is_horizontal):
    step = 1 if to_var > from_var else -1
    for var in range(from_var + step, to_var, step):
        if is_horizontal:
            if board.get_piece(from_fixed, var) is not None:
                return False
        else:
            if board.get_piece(var, from_fixed) is not None:
                return False
    return True

def is_path_clear_diagonal(board, from_row, from_col, to_row, to_col):
    row_step = 1 if to_row > from_row else -1
    col_step = 1 if to_col > from_col else -1
    row, col = from_row + row_step, from_col + col_step
    while row != to_row and col != to_col:
        if board.get_piece(row, col) is not None:
            return False
        row += row_step
        col += col_step
    return True

@staticmethod
def is_single_step_forward(context, direction):
    if context.from_row + direction == context.to_row:
        if context.board.get_piece(context.to_row, context.to_col) is None:
            return True
    return False

@staticmethod
def is_double_step_forward(context, direction, start_row):
    if context.from_row == start_row and context.from_row + 2 * direction == context.to_row:
        if context.board.get_piece(context.to_row, context.to_col) is None and context.board.get_piece(context.from_row + direction, context.to_col) is None:
            return True
    return False