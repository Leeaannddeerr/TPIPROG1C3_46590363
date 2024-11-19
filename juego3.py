import random

def elegir_palabra():
    palabras = ['python', 'programacion', 'cadena', 'matrices', 'paradigma']
    return random.choice(palabras)

def mostrar_hangman(intentos):
    estados = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    print(estados[intentos])

def ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos > 0:
        mostrar_hangman(intentos)
        
        # Mostrar el progreso
        progreso = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
        print(f"\nPalabra: {progreso}")
        print(f"Intentos restantes: {intentos}")

        # Solicitar una letra
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Prueba con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto!")
        else:
            print("Incorrecto.")
            intentos -= 1

        # Verificar si se adivinaron todas las letras
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
            break
    else:
        print(f"Perdiste. La palabra era: {palabra}")
        mostrar_hangman(0)  # Mostrar estado final

if __name__ == "__main__":
    ahorcado()