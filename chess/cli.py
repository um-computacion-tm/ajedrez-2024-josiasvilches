from chess.chess import *
from chess.exceptions import InvalidMoveError
from chess.board import *



def main():
    chess = Chess()

    print("Bienvenido al Ajedrez. Para salir, ingresa 'salir' en cualquier momento. \nBlancos empiezan, es decir los que están en mayúsculas.")
    
    while True:
        if not play(chess):
            break  # Si el jugador decide salir, termina el bucle

def play(chess):
    try:
        chess.display_board()
        # Input for movement
        from_row = input("From row: ")
        if from_row.lower() == "salir":
            return False
        
        from_col = input("From col: ")
        if from_col.lower() == "salir":
            return False
        
        to_row = input("To row: ")
        if to_row.lower() == "salir":
            return False
        
        to_col = input("To col: ")
        if to_col.lower() == "salir":
            return False
        
        # Converts inputs into ints
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)

        # Move piece
        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Movimiento No Valido")
        
    except ValueError:
        print("Entrada no válida. Por favor ingresa números enteros para las posiciones.")
    
    except InvalidMoveError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return True  # Continuar el juego

if __name__ == "__main__":
    main()


