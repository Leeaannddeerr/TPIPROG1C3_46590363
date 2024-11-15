# tablero
def P_board(board):  # Definimos la variable que utillizo para generara el tablero
    for row in board:  # Diseño el tablero para una mejor vista
        print(" | ".join(row))  # linea que separa las columnas  del tablero
        print("_" * 9)  # linea que separa las filas del tablero

# comprobacion del ganador


def Gg_win(board, Jugador):  # Defino otra variable para representar el ganador del juego
    # columnas y filas
    for row in board:  # repite cada fila del tablero
        # verifica si todos los espacios de la fila pertenecen al jugador
        if all([spot == Jugador for spot in row]):
            return True  # comprueba si una de las filas pertenecen al jugador,retorna True
    for col in range(3):  # repite cada columna del tablero
        # comprueba si todos los elementos pertenecen al jugador
        if all([board[row][col] == Jugador for row in range(3)]):
            return True  # si una columna completab pertenece al jugador,retorna True
    if all([board[i][i] == Jugador for i in range(3)]) or all([board[i][2 - i] == Jugador for i in range(3)]):  # comprueba las diagonales
        return True  # si alguna de las dos diagonales pertenece al jugador, retorna True
    return False  # si no hay ganador, retorna False

# Caso de empate


def Gg_Draw(board):  # defina la funcion para controlar si hay empate
    # Retorna el True si todos los espacios estan ocupados
    return all([spot != " " for row in board for spot in row])

# turnos


def jugador_V(board, Jugador):  # define la funcion para gestionar los movimientos del jugador
    while True:  # Ciclo infinito hasta que elija una posicion valida
        try:
            # pide al jugador que elija una posicion del 1 al 9
            Mover = int(
                input(f"jugador {Jugador},elige una posicion (1-9):")) - 1
            # calcula la posicion en el tablero y verifica si esta vacia
            if board[Mover // 3][Mover % 3] == " ":
                # Coloca la marca del jugador en la posicion elegida
                board[Mover // 3][Mover % 3] = Jugador
                break  # Sale del siclo si la posicion es valida
            else:

                # Mensaje si la posicion esta ocupada
                print("Posicion esta ocupada. selecione otra:")
        except (ValueError, IndexError):  # captura errores de entradas invalida
            # Mensaje si la entrada es invalida
            print("Tienes que elegir un numero del 1-9")

# Funcionamiento del juego


def inicio_j():  # inicia el tablero vacio de 3x3
    board = [[" "for _ in range(3)] for _ in range(3)]
    c_jugador = "❌"  # el primer jugador usa "X"
    while True:  # Bucle pricipal del juego
        P_board(board)  # muestra el tablero actual
        # llama a la funcion para que el jugador actual realice su turno
        jugador_V(board, c_jugador)
        if Gg_win(board, c_jugador):  # comprueba si el jugador actual gano el juego
            P_board(board)  # muestra el tablero final
            # anuncia el ganador del juego
            print(f"!Jugador {c_jugador} gano el juego¡")
            break  # termina el juego si hay un ganador
        elif Gg_Draw(board):  # conprueba si el juego termino en empate
            P_board(board)  # muestra el tablero final
            print("El juego termina en empate")  # anunci el empate
            break  # termina el juego si hay un empate
        # alterna los jugadores: si uno es "X", el otro es "O"y veceversa
        c_jugador = "⭕" if c_jugador == "❌" else "❌"


if __name__ == "__main__":  # ejecuta el juegos si el archivo fue ejecutado directamente

    inicio_j()  # Llama a la funcion para iniciar el juego
