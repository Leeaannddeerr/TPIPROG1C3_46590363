import time
import getpass
import random

def tiempo321(tiempo):
    print()
    for i in range(tiempo, 0, -1):
        print(str(i)+"...")
        time.sleep(1)

def quiengana():
    global mis_puntos
    global puntos_rival
    tiempo321(3)
    print()
    if jugador1[0] == "1" and jugador2[0] == "3":
            print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟙) 𝕊 𝕌 𝕄 𝔸: Piedra🪨  gana a Tijera✂️\n"+"*" * 50)
            mis_puntos = mis_puntos + 1
    elif jugador1[0] == "2" and jugador2[0] == "1":
            print("*" *50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟙) 𝕊 𝕌 𝕄 𝔸: Papel📜 gana a Piedra🪨\n"+"*" * 50)
            mis_puntos = mis_puntos + 1
    elif jugador1[0] == "3" and jugador2[0] == "2":
            print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ 𝟙 𝕊 𝕌 𝕄 𝔸: Tijera✂️  gana a Papel📜\n"+"*" * 50)
            mis_puntos = mis_puntos + 1
    elif jugador2[0] == "1" and jugador1[0] == "3":
            print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Piedra🪨  gana a Tijera✂️\n"+"*" * 50)
            puntos_rival = puntos_rival + 1
    elif jugador2[0] == "2" and jugador1[0] == "1":
            print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Papel📜 gana a Piedra🪨\n"+"*" * 50)
            puntos_rival = puntos_rival + 1
    elif jugador2[0] == "3" and jugador1[0] == "2":
            print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Tijera✂️  gana a Papel📜\n"+"*" * 50)
            puntos_rival = puntos_rival + 1 
    elif jugador1[0] > "0" and jugador1[0] < "4" and jugador2[0] > "0" and jugador2[0] < "4" and jugador1[0] == jugador2[0]:
            print("*" * 37,"\n   𝔼 𝕄 ℙ 𝔸 𝕋 𝔼:   ℕ 𝔸 𝔻 𝕀 𝔼   𝕊 𝕌 𝕄 𝔸\n"+"*" * 37) 
    else:
         print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n\n               ⚠️               \n  Un jugador ingresó una opción\n  incorrecta, nadie suma en esta\n              ronda.\n \n   Selecciona correctamente:\n   1=Piedra, 2=Papel, 3=Tijera.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def mostrarpuntos():
      if mis_puntos < puntos and puntos_rival < puntos:
        print("︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 1: {mis_puntos}\n"+"︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 2: {puntos_rival}\n"+"︵‿︵‿︵‿︵" * 2,"\n"+"\n"f"➢ La partida acabará cuando uno de los dos jugadores llegue a {puntos} puntos.\n ")
      elif mis_puntos == puntos or puntos_rival == puntos:
        print("︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 1: {mis_puntos}\n"+"︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 2: {puntos_rival}\n"+"︵‿︵‿︵‿︵" * 2,"\n"+"\n"f"➣ El ganador de esta ronda llegó a los {puntos} puntos y finalizó la partida.\n ")
opcion = 1  
while opcion != 0:
    #aca iria el menu 
    print("1-Piedra, Papel o Tijera \n2-Ahorcado\n3-Tres en Raya\n0-Salir")
    opcion=int(input())
    if opcion == 1:
        juego = 0 #Se declara esta variable en 0 para poder entrar al while y preguntarle al usuario que modo de juego quiere
        puntos = 0 #Esta variable es donde se guardaran los puntos a jugar en la partida. El jugador que iguale primero al valor guardado en puntos será el ganador.
        while juego != 3:
            #Se muestra en pantalla el menu del juego y sus opciones (jugar con ammigo, jugar con pc o volver al menu principal). Luego el usuario ingresara una de las opciones. En caso de equivocarse se le pide que ingrese nuevamente.
            print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n\n    1- Jugar con un amigo🫂\n\n    2- Jugar contra la PC🤖\n\n    3- Salir del juego🚪\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            juego= int(input("Seleccione una opción: "))
            if juego == 3:
             print(" \nVolviendo al menú principal...\n ")
             time.sleep(3) 
             break
            elif juego == 1 or juego == 2:
             print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n \n ¿A cuantos puntos desea jugar?\n \n        🪨     📜    ✂️\n \n        Recomendado: 3🔥\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
             puntos = int(input("Ingrese los puntos a jugar: "))
            else:
             print("\n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n              ⚠️               \n       Opcion incorrecta.\n  Porfavor vuelva a intentarlo.\n \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")   
            if puntos > 0 and puntos <11:
                mis_puntos = 0
                puntos_rival = 0
                control = True
                while control == True:
                        if (mis_puntos < puntos and puntos_rival < puntos):  
                            if juego ==1:
                                print()
                                jugador1 = getpass.getpass("Jugador 1:  1=Piedra, 2=Papel, 3=Tijera: ")
                                jugador2 = getpass.getpass("Jugador 2:  1=Piedra, 2=Papel, 3=Tijera: ")
                                quiengana()
                                mostrarpuntos()
                            elif juego == 2:
                                opciones = ["1", "2", "3"]
                                print()
                                jugador1 = input("Jugador 1:  1=Piedra, 2=Papel, 3=Tijera: ")
                                jugador2 = random.choice(opciones)
                                quiengana()
                                mostrarpuntos()
                            elif juego == 3:
                                print("Volviendo al menu principal...")
                                time.sleep(3)
                                control = False
                            else:
                                print("Error. Opcion Incorrecta.")    
                        elif mis_puntos == puntos:
                                print("Ganador: Jugador 1.\nGracias por jugar.\n ")
                                time.sleep(6)
                                print("Volviendo al menu del juego...")
                                time.sleep(3)
                                control = False
                        elif puntos_rival == puntos:
                                print("Ganador: Jugador 2.\nGracias por jugar.\n ")
                                time.sleep(6)
                                print("Volviendo al menu del juego...")
                                time.sleep(3)
                                control = False           
            elif puntos <=0 or puntos >10:
               if juego == 1 or juego ==2:
                print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n              ⚠️        \n  Los puntos a jugar deben ser\n  minimo de 1 y maximo de 10\n  para una mejor experiencia. \n\n  Porfavor vuelva a intentarlo.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                time.sleep(3)
    else:
             pass                                                  