import TPIjeringoso
import TPI_escalones_Gastón_Godoy_Dechecco as escalones


def menu():
    print("Bienvenido a los 6 juegos")
    print("""
        Presione 0 para salir
        Presione 1- Piedra, papel, tijera
        presione 2- Jeringoso
        Presione 3- 5 Escalones
        Presione 4- ?
        Presione 5- ?
        Presione 6- ?
        """)
    usuario = ""
    tupla = ("0","1","2","3","4","5","6")
    while usuario not in tupla: 
        usuario = input("Ingrese una opción: ")
        if usuario == "0":
            print("Gracias por jugar")
        elif usuario == "1":
            pass
        elif usuario == "2":
            TPIjeringoso
        elif usuario == "3":
            escalones
        elif usuario == "4":
            pass
        elif usuario == "5":
            pass
        elif usuario == "6":
            pass

if __name__ == "__main__":
    menu()
