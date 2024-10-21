class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class PathDetails:
    def __init__(self, fixed, var, step):
        self.fixed = fixed
        self.var = var
        self.step = step

class ContextBase:
    def __init__(self, board):
        self.board = board

class BoardContext(ContextBase):
    def __init__(self, board, path_details, is_horizontal):
        super().__init__(board)
        self.path_details = path_details
        self.is_horizontal = is_horizontal

class DiagonalContext(ContextBase):
    def __init__(self, board, from_position, to_position, steps):
        super().__init__(board)
        self.from_position = from_position
        self.to_position = to_position
        self.steps = steps

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
    path_details = PathDetails(from_fixed, from_var, step)
    path_context = BoardContext(board, path_details, is_horizontal)
    return check_linear_path_clear(path_context, to_var)

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

def check_linear_path_clear(path_context, to_var):
    """
    Verifica si el camino está despejado entre las posiciones variables.
    """
    for var in range(path_context.path_details.var + path_context.path_details.step, to_var, path_context.path_details.step):
        position = Position(path_context.path_details.fixed, var) if path_context.is_horizontal else Position(var, path_context.path_details.fixed)
        if path_context.board.get_piece(position) is not None:
            return False
    return True

def is_path_clear_diagonal(context):
    """
    Verifica si el camino está despejado en una diagonal.
    """
    board = context.game_context.board  # Acceder al tablero desde game_context
    steps = get_diagonal_steps(context)
    path_context = DiagonalContext(board, context.from_position, context.to_position, steps)
    return check_diagonal_path_clear(path_context)

def get_diagonal_steps(context):
    """
    Obtiene los pasos para iterar sobre el camino diagonal.
    """
    row_step = 1 if context.to_position.row > context.from_position.row else -1
    col_step = 1 if context.to_position.col > context.from_position.col else -1
    return row_step, col_step

def check_diagonal_path_clear(path_context):
    """
    Verifica si el camino está despejado en una diagonal.
    """
    row, col = path_context.from_position.row + path_context.steps[0], path_context.from_position.col + path_context.steps[1]
    while row != path_context.to_position.row and col != path_context.to_position.col:
        position = Position(row, col)
        if path_context.board.get_piece(position) is not None:
            return False
        row += path_context.steps[0]
        col += path_context.steps[1]
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