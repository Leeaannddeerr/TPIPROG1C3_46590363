# tablero
def P_board(board):  # Definimos la variable que utillizo para generara el tablero
    for row in board:  # Diseño el tablero para una mejor vista
        print(" | ".join(row))  # linea que separa las columnas  del tablero
        print("_" * 9)  # linea que separa las filas del tablero

# comprobacion del ganador


def Gg_win(board, Jugador):  # Defino otra variable para representar el ganador del juego
    # columnas y filas
    for row in board:
        if all([spot == Jugador for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == Jugador for row in range(3)]):
            return True
    if all([board[i][i] == Jugador for i in range(3)]) or all([board[i][2 - i] == Jugador for i in range(3)]):
        return True
    return False

# Caso de empate


def Gg_Draw(board):
    return all([spot != " " for row in board for spot in row])

# turnos


def jugador_V(board, Jugador):
    while True:
        try:
            Mover = int(
                input(f"jugador {Jugador},elige una posicion (1-9):")) - 1
            if board[Mover // 3][Mover % 3] == " ":
                board[Mover // 3][Mover % 3] = Jugador
                break
            else:
                print("Posicion esta ocupada. selecione otra:")
        except (ValueError, IndexError):
            print("Tienes que elegir un numero del 1-9")

# Funcionamiento del juego


def inicio_j():
    board = [[" "for _ in range(3)] for _ in range(3)]
    c_jugador = "❌"
    while True:
        P_board(board)
        jugador_V(board, c_jugador)
        if Gg_win(board, c_jugador):
            P_board(board)
            print(f"!Jugador {c_jugador} gano el juego¡")
            break
        elif Gg_Draw(board):
            P_board(board)
            print("El juego termina en empate")
            break
        c_jugador = "⭕" if c_jugador == "❌" else "❌"


if __name__ == "__main__":

    inicio_j()

