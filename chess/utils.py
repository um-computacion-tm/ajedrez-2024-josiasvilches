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
    """
    Verifica si el camino está despejado en una línea recta (horizontal o vertical).
    """
    board = context.game_context.board  # Acceder al tablero desde game_context
    from_fixed, from_var, to_var = get_fixed_and_variable_positions(context, is_horizontal)
    step = get_step(from_var, to_var)
    return check_linear_path_clear(board, from_fixed, from_var, to_var, step, is_horizontal)

def get_fixed_and_variable_positions(context, is_horizontal):
    """
    Obtiene las posiciones fijas y variables para el movimiento lineal.
    """
    from_fixed = context.from_position.row if is_horizontal else context.from_position.col
    from_var = context.from_position.col if is_horizontal else context.from_position.row
    to_var = context.to_position.col if is_horizontal else context.to_position.row
    return from_fixed, from_var, to_var

def get_step(from_var, to_var):
    """
    Obtiene el paso para iterar sobre el camino.
    """
    return 1 if to_var > from_var else -1

def check_linear_path_clear(board, from_fixed, from_var, to_var, step, is_horizontal):
    """
    Verifica si el camino está despejado entre las posiciones variables.
    """
    for var in range(from_var + step, to_var, step):
        position = Position(from_fixed, var) if is_horizontal else Position(var, from_fixed)
        if board.get_piece(position) is not None:
            return False
    return True

def is_path_clear_diagonal(context):
    """
    Verifica si el camino está despejado en una diagonal.
    """
    board = context.game_context.board  # Acceder al tablero desde game_context
    row_step, col_step = get_diagonal_steps(context)
    return check_diagonal_path_clear(board, context.from_position, context.to_position, row_step, col_step)

def get_diagonal_steps(context):
    """
    Obtiene los pasos para iterar sobre el camino diagonal.
    """
    row_step = 1 if context.to_position.row > context.from_position.row else -1
    col_step = 1 if context.to_position.col > context.from_position.col else -1
    return row_step, col_step

def check_diagonal_path_clear(board, from_position, to_position, row_step, col_step):
    """
    Verifica si el camino está despejado en una diagonal.
    """
    row, col = from_position.row + row_step, from_position.col + col_step
    while row != to_position.row and col != to_position.col:
        position = Position(row, col)
        if board.get_piece(position) is not None:
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