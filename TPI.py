#importamos para utilizar las funciones en el codigo
import time
import getpass
import random
import Menu

def errores_ejecucion(error): #funcion definida para ahorrar el mismo print en ciertas partes del codigo cuando usemos el control de las excepciones.
    global mi_try_control #declaramos la variable como global asi el subprograma puede conocerla y trnajar con ella.
    mi_try_control = True #mi_try_control cambia su valor booleano.
    if error == "Keyboard": #manejo de excepcion "Ctrl + C"
      print(" \n \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n              ⚠️        \n            ¡ERROR!\n Para salir del juego presione \n    la opción 3 en el menú.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    elif error == "Value" or error == "Index": #manejo de expecion para valueerror y indexerror
      print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n              ⚠️        \n            ¡ERROR!\n  Presionaste incorrectamente, \n      vuelve a intentarlo.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(2) #tiempo para leer el error antes de continuar

def tiempo321(segundos): #Tiene como parametro formal la variable que se utilizará dentro de esta función llamada "segundos". 
    print() #este print hace un enter para separar lo que este arriba y se vea más prolijo.
    for i in range(segundos, 0, -1): #el ciclo for va desde el valor tomado por "segundos" hasta 0 sin incluirlo y con paso negativo para ejecutarse correctamente.
        print(str(i)+"...") #se imprime el valor de i actual seguido de puntos suspensivos.
        time.sleep(1) #aca es donde verdaramente transcurre el segundo. 

def quiengana(j_1, j_2): #el parametro actual de jugador_1 y jugador_2 fueron reemplazados en la función por el parametro formal j_1 y j_2, esto está hecho para ahorrarnos caracteres en el codigo.
    global mis_puntos #se declara a estas dos variables como globales para que el sub-programa las conozca y pueda trabajar con ellas modificando su valor.
    global puntos_rival
    tiempo321(3) #se llama a la funcion tiempo y se le pasa como parametro actual el numero 3 que será el tiempo a mostrar antes de saber quien ganó la ronda.
    print() #este print separa la funcion de arriba con el texto que se muestra a continuación:    
    try: #manejo de excepcion en la suma de puntos
      if j_1[0] == "1" and j_2[0] == "3":
        print("*" * 53,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟙) 𝕊 𝕌 𝕄 𝔸: Piedra🪨  gana a Tijera✂️\n"+"*" * 53)
        mis_puntos = mis_puntos + 1
      elif j_1[0] == "2" and j_2[0] == "1":
        print("*" *50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟙) 𝕊 𝕌 𝕄 𝔸: Papel📜 gana a Piedra🪨\n"+"*" * 50)
        mis_puntos = mis_puntos + 1
      elif j_1[0] == "3" and j_2[0] == "2":
        print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟙) 𝕊 𝕌 𝕄 𝔸: Tijera✂️  gana a Papel📜\n"+"*" * 50)
        mis_puntos = mis_puntos + 1
      elif j_2[0] == "1" and j_1[0] == "3":
        print("*" * 53,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Piedra🪨  gana a Tijera✂️\n"+"*" * 53)
        puntos_rival = puntos_rival + 1
      elif j_2[0] == "2" and j_1[0] == "1":
        print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Papel📜 gana a Piedra🪨\n"+"*" * 50)
        puntos_rival = puntos_rival + 1
      elif j_2[0] == "3" and j_1[0] == "2":
        print("*" * 50,"\n𝕁 𝕌 𝔾 𝔸 𝔻 𝕆 ℝ (𝟚) 𝕊 𝕌 𝕄 𝔸: Tijera✂️  gana a Papel📜\n"+"*" * 50)
        puntos_rival = puntos_rival + 1 
      elif j_1[0] > "0" and j_1[0] < "4" and j_2[0] > "0" and j_2[0] < "4" and j_1[0] == j_2[0]:
        print("*" * 44,"\n   𝔼 𝕄 ℙ 𝔸 𝕋 𝔼:   ℕ 𝔸 𝔻 𝕀 𝔼   𝕊 𝕌 𝕄 𝔸 🤝\n"+"*" * 44) 
      else: #en caso de que un usuario no haga una elección correcta se le mostrará el siguiente mensaje y ninguno sumará en la ronda:
        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n\n               ⚠️               \n  Un jugador ingresó una opción\n  incorrecta, nadie suma en esta\n              ronda.\n \n   Selecciona correctamente:\n   1=Piedra, 2=Papel, 3=Tijera.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    except IndexError:
       errores_ejecucion("Index")
    except KeyboardInterrupt:
       errores_ejecucion("Keyboard")  

def mostrarpuntos(mis_puntos, puntos_rival, puntos): #funcion para mostrar los puntos del usuario y del rival.
  if mis_puntos < puntos and puntos_rival < puntos:
    print("︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 1: {mis_puntos}\n"+"︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 2: {puntos_rival}\n"+"︵‿︵‿︵‿︵" * 2,"\n"+"\n"f"➢ La partida acabará cuando uno de los dos jugadores llegue a {puntos} puntos. 💥\n ")
  elif mis_puntos == puntos or puntos_rival == puntos:
    print("︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 1: {mis_puntos}\n"+"︵‿︵‿︵‿︵" * 2,"\n"f"Puntos del jugador 2: {puntos_rival}\n"+"︵‿︵‿︵‿︵" * 2,"\n"+"\n"f"➣ El ganador de esta ronda llegó a los {puntos} puntos y finalizó la partida. 💥\n ")

puntos = 0 #Esta variable es donde se guardaran los puntos a jugar en la partida. El jugador que iguale primero al valor guardado en puntos será el ganador.
mis_puntos = 0 #en esta variable se acumularan los puntos del jugador 1.
puntos_rival = 0 #en esta variable se acumularan los puntos del jugador 2 o la PC.
  
def LeanPiedraPapelTijera():
 juego = 0 #Se declara esta variable en 0 para poder entrar al while y preguntarle al usuario que modo de juego quiere
 while juego != 3:
   global mis_puntos, puntos_rival, puntos
   juego = 0
   mis_puntos = 0
   puntos_rival = 0
   #Se muestra en pantalla el menu del juego y sus opciones (jugar con amigo, jugar con pc o volver al menu principal). Luego el usuario ingresara una de las opciones. En caso de equivocarse se le pide que ingrese nuevamente.
   print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n\n    1- Jugar con un amigo🫂\n\n    2- Jugar contra la PC🤖\n\n    3- Salir del juego🚪\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
   mi_try_control = False #variable que ayudará a ejecutar las excepciones correctamente
   try: #manejo de excepciones en el menu del juego
       juego= int(input("Seleccione una opción: "))
   except ValueError:
     errores_ejecucion("Value")
   except KeyboardInterrupt:
     errores_ejecucion("Keyboard")
   if juego == 3: #si el jugador selecciona la opcion 3, saldremos del ciclo repetitvo "mientras" y volveremos al menú principal.
     print(" \nVolviendo al menú principal...\n ")
     time.sleep(3)
     Menu.menu() #vuelve al menu
     break #este break sirve para salir del codigo inmediatamente y que no se evaluen otros condicionales. 
   elif juego == 1 and mi_try_control == False or juego == 2 and mi_try_control == False:
     try: #manejo de excepciones en donde se eligen los puntos a jugar
       print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n \n ¿A cuantos puntos desea jugar?\n \n        🪨     📜    ✂️\n \n        Recomendado: 3🔥\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
       puntos = 0
       puntos = int(input("Ingrese los puntos a jugar: ")) #aca el usuario ingresara los puntos a jugar (lo permitido es entre 1 y 10, en caso de equivocarse se le volvera a pedir)
       if puntos <= 0 or puntos > 10:
        print(" \n「 ✦ 𝒫𝒾𝑒𝒹𝓇𝒶, 𝒫𝒶𝓅𝑒𝓁 𝑜 𝒯𝒾𝒿𝑒𝓇𝒶 ✦ 」\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n              ⚠️        \n  Los puntos a jugar deben ser\n  minimo de 1 y maximo de 10\n  para una mejor experiencia. \n\n  Porfavor vuelva a intentarlo.\n\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        time.sleep(4) #tiempo para que el jugador lea el mensaje antes de volver al menú del juego.
     except ValueError:
        errores_ejecucion("Value")
     except KeyboardInterrupt:
       errores_ejecucion("Keyboard")
   if puntos > 0 and puntos <11: #si los puntos elegidos son correctos, inicia el juego.
        control = True #esta variable se inicializa en True para estar dentro del siguiente ciclo while.
        while control == True: #si control es true, el codigo se seguirá ejecutando, si es false saldrá del ciclo.
          if (mis_puntos < puntos and puntos_rival < puntos):  
            if juego ==1: #si el usuario elegió la opcion 1 significa que jugará contra otro jugador real
                try: #manejo de excepciones en modo de juego "Jugar con un amigo"
                  #print() #el print hace un enter para separar el texto de arriba con las opciones de abajo (esto facilita la legibilidad del codigo). **fue reemplazado por un \n que cumple la misma funcion** 
                  jugador1 = getpass.getpass("\nJugador 1:  1=Piedra, 2=Papel, 3=Tijera: ") #el getpass.getpass sirve para que no se vea lo que esta ingresando el usuario 
                  #print() #este print separa en la terminal las elecciones de los dos jugadores para que sea mas estetico  **fue reemplazado por un \n que cumple la misma funcion**
                  jugador2 = getpass.getpass("\nJugador 2:  1=Piedra, 2=Papel, 3=Tijera: ")
                  quiengana(jugador1,jugador2) #llamamos a la funcion para mostrar el resultado de la ronda y le pasamos los parametros actuales que ingresó cada jugador.
                  mostrarpuntos(mis_puntos, puntos_rival, puntos) #llamamos a esta funcion para mostrar el progreso actual de la partida.
                except KeyboardInterrupt:
                   errores_ejecucion("Keyboard")              
            elif juego == 2: #si opcion es 2 significa que el usuario quiere jugar contra un jugador no real (la pc).
                  try: #manejo de excepciones en modo de juego "Jugar contra la PC"
                    opciones = ["1", "2", "3"] #la pc elegirá de forma aleatoria gracias al import random y funcion random.choice uno de estos elementos dentro de la estructura dinamica "Lista".
                    jugador1 = input("\nJugador 1🎮:  1=Piedra🪨  2=Papel📜 3=Tijera✂️ : ") #turno del jugador 1 para elegir.
                    jugador2 = random.choice(opciones) #turno de la pc para elegir.
                    quiengana(jugador1, jugador2) 
                    mostrarpuntos(mis_puntos, puntos_rival, puntos)
                  except KeyboardInterrupt:
                     errores_ejecucion("Keyboard")
            elif juego == 3: #si en el menú del juego el usuario ingresa la opción 3 significa que no quiere jugar, por lo cual se lo llevará al menú principal.
                  print("Volviendo al menu principal...")
                  time.sleep(3) #gracias al import time y funcion time.sleep podemos hacer un regreso más lento para aumentar la realidad de nuestro codigo (simulando la carga del programa).
                  control = False #modificamos el valor booleano de control para salir del ciclo.                
            else:
              control = False      
          elif mis_puntos == puntos: #si el jugador 1 llega a los puntos necesarios para ganar, la partida finalizará y se mostrara el siguiente print.
            time.sleep(4) #tiempo para que se lean los puntos, el jugador que suma y la finalizacion de la partida antes de mostrar el mensaje del ganador
            print("      ⚔️ 𝐹𝒾𝓃 𝒹𝑒 𝓁𝒶 𝓅𝒶𝓇𝓉𝒾𝒹𝒶⚔️\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n \n      Ganador: Jugador 1. 🏆\n \n         🪨     📜    ✂️\n \n      Gracias por jugar. 🫶\n \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
            time.sleep(6)  #Luego de los 6 segundos que tiene el usuario para leer el mensaje, se le informará con el siguiente print que está siendo dirigido al menú del juego nuevamente.
            print("Volviendo al menu del juego...\n")
            time.sleep(3) #tiempo para que el jugador lea el mensaje antes de volver al menú del juego.
            control = False #se modifica la variable control para salir del ciclo while y volver al menú del juego.
          elif puntos_rival == puntos: #si el jugador 2 llega a los puntos necesarios para ganar, la partida finalizará y se mostrara lo mismo que en el caso del jugador 1.                        time.sleep(4)
            time.sleep(4)
            print("      ⚔️ 𝐹𝒾𝓃 𝒹𝑒 𝓁𝒶 𝓅𝒶𝓇𝓉𝒾𝒹𝒶⚔️\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n \n      Ganador: Jugador 2. 🏆\n \n         🪨     📜    ✂️\n \n      Gracias por jugar. 🫶\n \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
            time.sleep(6)
            print("Volviendo al menu del juego...\n")
            time.sleep(3) 
            control = False

if __name__ == "__main__":
    LeanPiedraPapelTijera()