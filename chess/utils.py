class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class GameContext:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn

class MoveContext:
    def __init__(self, game_context, piece, from_position, to_position):
        self.game_context = game_context
        self.piece = piece
        self.from_position = from_position
        self.to_position = to_position

def is_path_clear_linear(context, is_horizontal):
    board = context.game_context.board  # Acceder al tablero desde game_context
    from_fixed = context.from_position.row if is_horizontal else context.from_position.col
    from_var = context.from_position.col if is_horizontal else context.from_position.row
    to_var = context.to_position.col if is_horizontal else context.to_position.row
    step = 1 if to_var > from_var else -1
    for var in range(from_var + step, to_var, step):
        position = Position(from_fixed, var) if is_horizontal else Position(var, from_fixed)
        if board.get_piece(position) is not None:
            return False
    return True

def is_path_clear_diagonal(context):
    row_step = 1 if context.to_position.row > context.from_position.row else -1
    col_step = 1 if context.to_position.col > context.from_position.col else -1
    row, col = context.from_position.row + row_step, context.from_position.col + col_step
    while row != context.to_position.row and col != context.to_position.col:
        position = Position(row, col)
        if context.game_context.board.get_piece(position) is not None:
            return False
        row += row_step
        col += col_step
    return True

@staticmethod
def is_single_step_forward(context, direction):
    if context.from_position.row + direction == context.to_position.row:
        if context.game_context.board.get_piece(context.to_position) is None:
            return True
    return False

@staticmethod
def is_double_step_forward(context, direction, start_row):
    if context.from_position.row == start_row and context.from_position.row + 2 * direction == context.to_position.row:
        if context.game_context.board.get_piece(context.to_position) is None and context.game_context.board.get_piece(Position(context.from_position.row + direction, context.to_position.col)) is None:
            return True
    return False