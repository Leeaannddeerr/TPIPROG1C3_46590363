import TPIjeringoso
import TPI_5Escalones 
import Tres_en_Raya
import TPI
import juego3

def menu():
  print("""
            𝓑𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 
                 𝓪  
       🇻  🇱  🇦  🇬  🇬  🇦  🇲  🇪  🇸 
╔════.✵.═════════════════════════════╗

    0- Salir. 🚪
          
    1- Piedra🪨, Papel📜 o Tijera✂️
          
    2- Jeringoso 😎
          
    3- Los 5 Escalones 🪜
          
    4- El Ahorcado 🪢
          
    5- Ta-Te-Ti ❌⭕❌
          
╚════════════════════════════════.✵.═╝                 
        """)
  
  usuario = ""
  tupla = ("0","1","2","3","4","5")
  while usuario not in tupla: 
    try:
      usuario = input("Ingrese una opción: ")
    except KeyboardInterrupt:
      print("Error, para salir presione: 0 ")
    if usuario == "1":
      TPI.LeanPiedraPapelTijera()
    elif usuario == "2":
      TPIjeringoso.main()
    elif usuario == "3":
      TPI_5Escalones.general()
    elif usuario == "4":
      juego3.ahorcado()
    elif usuario == "5":
      Tres_en_Raya.inicio_j()
    elif usuario == "0":
      print("""
       🇻  🇱  🇦  🇬  🇬  🇦  🇲  🇪  🇸 
╔═.✵.════════════════════════════════╗

        🔥GRACIAS POR JUGAR🔥 
          
╚════════════════════════════════.✵.═╝              
   
        """)

if __name__ == "__main__":
  menu()
