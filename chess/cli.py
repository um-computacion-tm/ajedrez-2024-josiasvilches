from chess.chess import *
from chess.exceptions import *
from chess.board import *
from chess.pieces import *
from chess.movements import *
from chess.utils import *

# Main function
def main():
    '''
    The function main() is the entry point of the program.
    '''
    chess = Chess()

    print("Bienvenido al Ajedrez. Para salir, ingresa 'salir' en cualquier momento. \nBlancos empiezan\n¡Que gane el mejor!")
    
    while True:
        try:
            if not play(chess):
                break
        except (GameOverException, KingisDeadException) as e:
            print(str(e))
            break

# Get user input for a move
def get_user_input():
    '''
    The function get_user_input() prompts the user to enter the coordinates of the piece they want to move and its destination.
    It allows the user to exit the game by entering 'salir'.
    Returns:
        from_row, from_col, to_row, to_col: The coordinates of the piece to move and its destination.
    '''
    inputs = ["From row (0-7): ", "From col (a-h): ", "To row (0-7): ", "To col (a-h): "]
    results = []

    for prompt in inputs:
        user_input = input(prompt).lower()
        if user_input == "salir":
            return None, None, None, None
        results.append(user_input)
    
    return results
# Convert user input to board indices
def convert_input_to_indices(from_row, from_col, to_row, to_col):
    '''
    The function convert_input_to_indices() converts the user input coordinates to board indices.
    Parameters:
        from_row, from_col, to_row, to_col: The coordinates of the piece to move and its destination.
    Returns:
        from_row, from_col, to_row, to_col: The converted coordinates as board indices.
    Raises:
        InvalidInputError: If the input is not valid.
    '''
    try:
        from_row = int(from_row)
        from_col = ord(from_col) - ord('a')
        to_row = int(to_row)
        to_col = ord(to_col) - ord('a')
    except ValueError:
        raise InvalidInputError()
    
    return from_row, from_col, to_row, to_col

# Check for game over
def check_game_over(chess):
    '''
    The function check_game_over() checks if the game is over by counting the pieces of each color.
    Parameters:
        chess: The chess game instance.
    Raises:
        GameOverException: If all pieces of one color have been eliminated.
    '''
    white_count, black_count = chess.count_pieces()
    if white_count == 0:
        print("Las piezas blancas han sido eliminadas. ¡Las negras ganan!")
        raise GameOverException()
    elif black_count == 0:
        print("Las piezas negras han sido eliminadas. ¡Las blancas ganan!")
        raise GameOverException()

# Handle user move
def handle_user_move(chess):
    '''
    The function handle_user_move() handles the user input and moves the piece on the board.
    Parameters:
        chess: The chess game instance.
    Returns:
        False if the user wants to exit the game, True otherwise.
    '''
    from_row, from_col, to_row, to_col = get_user_input()
    if from_row is None:
        print("Game over.")
        return False
    
    from_row, from_col, to_row, to_col = convert_input_to_indices(from_row, from_col, to_row, to_col)
    
    chess.move(from_row, from_col, to_row, to_col)
    
    check_game_over(chess)
    
    return True

# Chess game
def play(chess):
    '''
    The function play() handles the main game loop, displaying the board, getting user input, and making moves.
    Parameters:
        chess: The chess game instance.
    '''
    game_active = True
    while game_active:
        try:
            chess.display_board()
            print("Turn:", chess.get_turn())
            
            game_active = handle_user_move(chess)
        
        except (InvalidInputError, InvalidMoveError, OutOfBoundsError, NotYourTurnError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()