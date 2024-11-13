import TPIjeringoso
import TPI_escalones_Gastón_Godoy_Dechecco as escalones
import TPI_tres_en_raya

def menu():
    print("Bienvenido a los 5 juegos")
    print("""
        Presione 0 para salir 📤
        Presione 1- Piedra, Papel, Tijera🪨🧻✂️
        presione 2- Jeringoso😎
        Presione 3- 5 Escalones🪜
        Presione 4- El ahorcado🪢
        Presione 5- Ta-Te-Ti🙈🙉🙊
        """)
    usuario = ""
    tupla = ("0","1","2","3","4","5")
    while usuario not in tupla: 
        usuario = input("Ingrese una opción: ")
        if usuario == "0":
            print("Gracias por jugar🌻")
        elif usuario == "1":
            pass
        elif usuario == "2":
            TPIjeringoso.main()
        elif usuario == "3":
            escalones.general()
        elif usuario == "4":
            pass
        elif usuario == "5":
            TPI_tres_en_raya.inicio_j()

if __name__ == "__main__":
    menu()
