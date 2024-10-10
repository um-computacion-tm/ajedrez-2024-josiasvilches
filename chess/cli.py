from chess.chess import *
from chess.exceptions import InvalidMoveError
from chess.board import *
from chess.pieces import *
from chess.movements import *



def main():
    chess = Chess()

    print("Bienvenido al Ajedrez. Para salir, ingresa 'salir' en cualquier momento. \nBlancos empiezan, es decir los que están en mayúsculas.")
    
    while True:
        if not play(chess):
            break  # Si el jugador decide salir, termina el bucle

def play(chess):
    try:
        chess.display_board()
        # Input for movement (converting traditional chess notation)
        from_row = input("From row (0-7): ")
        if from_row.lower() == "salir":
            return False
        
        from_col = input("From col (a-h): ").lower()
        if from_col.lower() == "salir":
            return False
        
        to_row = input("To row (0-7): ")
        if to_row.lower() == "salir":
            return False
        
        to_col = input("To col (a-h): ").lower()
        if to_col.lower() == "salir":
            return False
        
        # Convert the row and column inputs to the board indices
        from_row = int(from_row)  # Rows are input as 1-8, so we subtract 1
        from_col = ord(from_col) - ord('a')  # Convert 'a'-'h' to 0-7 using ASCII values
        to_row = int(to_row)  # Rows are input as 1-8, so we subtract 1
        to_col = ord(to_col) - ord('a')  # Convert 'a'-'h' to 0-7 using ASCII values

        # Move piece
        chess.move(from_row, from_col, to_row, to_col)

    except ValueError:
        print("Entrada no válida. Por favor ingresa números enteros para las filas y letras para las columnas.")
    
    except InvalidMoveError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return True  # Continuar el juego

if __name__ == "__main__":
    main()