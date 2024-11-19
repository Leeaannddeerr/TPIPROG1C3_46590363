import Menu    #Se importa para volver al menu de los juegos

def respuesta(correcta,escalon,pregunta):
    with open(f"Archivos5escalones\{escalon}.txt", encoding="utf8") as archivo:  #Se abre el archivo.txt para mostrar las preguntas correspondientes al escalon
        archivo = archivo.read().split("///")
        print (archivo[pregunta]) 
    usuario = input("Seleccione a, b, c o d (x para salir): ")                 #Se pide que se ingrese una respuesta
    while "a" != usuario != "b" and "c" != usuario != "d" and "x" != usuario:
        usuario = input("Por favor seleccione a, b, c o d (x para salir): ")  
    if usuario == correcta:
        print("✅ Correcta✅")        #Si la respuesta es correcta retorna True, sino False o se puede volver al menu 
        return True 
    elif usuario == "x":
        Menu.menu()                    
    else:
        print("❌ Incorrecta❌")
        return False

def seguir(cont,siguiente):
    if cont >= 3:
        print("\nFelicitaciones, pasaste al siguiente escalon 🎉")  #Si hay 3 preguntas respondidas correctamente pasa al siguiente escalon
        print(f"Respondiste bien {cont} preguntas!\n")
        siguiente()
    else:
        print("\nNo pasas al siguiente escalon :(")
        print(f"Respondiste bien {cont} preguntas\n")                       #Si hay menos de 3 preguntas respondidas correctamente se pregunta si se quiere reintentar
        usuario = input("¿Desea reintentar el juego? (si o no)").lower()    #Si se desea volver a intentar comienza el juego desde 0
        while "si" != usuario != "no":                                      #Si se ingresa "no" se vuelve al menu
            usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        if usuario == "si":
            general()
        else:
            print("Gracias por jugar!")
            Menu.menu()

def animales():  #escalon 1
    contador = 0
    print("Bienvenido al escalon de animales 🐾")
    respuestas_correctas = ("a","d","b","d","c")    #Son las respuestas de cada una de las preguntas
    for i in range (5):
        if respuesta(respuestas_correctas[i],"Animales",i): #Al retornar True le suma 1 al contador
            contador += 1                           
    seguir(contador,geografia)

def geografia():  #escalon 2
    contador = 0
    print("Bienvenido al escalon de geografia 🌎")
    respuestas_correctas = ("c","a","a","b","d")
    for i in range (5):
        if respuesta(respuestas_correctas[i],"Geografia",i):
            contador += 1
    seguir(contador,historia)

def historia():  #escalon 3
    contador = 0
    print("Bienvenido al escalon de historia 📜")
    respuestas_correctas = ("b","c","c","c","a")
    for i in range (5):
        if respuesta(respuestas_correctas[i],"Historia",i):
            contador += 1
    seguir(contador,entretenimiento)

def entretenimiento():  #escalon 4
    contador = 0
    print("Bienvenido al escalon de entretenimiento 🕹️")
    respuestas_correctas = ("d","c","b","a","d")
    for i in range (5):
        if respuesta(respuestas_correctas[i],"Entretenimiento",i):
            contador += 1
    seguir(contador,aleatorias)

def aleatorias():  #escalon 5
    contador = 0
    print("Bienvenido al escalon de preguntas aleatorias 🎲")
    respuestas_correctas = ("b","c","b","a","d")
    for i in range (5):
        if respuesta(respuestas_correctas[i],"Aleatorias",i):
            contador += 1
    if contador >= 3:                                                       #En este escalon no se llama a la funcion siguiente() porque no hay mas escalones   
        print("\n🎊 Felicitaciones, ganaste el juego 🎊")                  #Si se responden 3 o mas preguntas correctamente gana el juego, sino puede volver a reintentar o volver al menu
        print(f"Respondiste bien {contador} preguntas\n")
        usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        while "si" != usuario != "no":
            usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        if usuario == "si":
            general()
        else:
            print("Gracias por jugar!")
            Menu.menu()

def general():
    print("Bienvenido a los 5 escalones")
    print("""
    Reglas del juego:
    - Son 5 escalones, cada escalon es una tematica diferente y tienen 5 preguntas cada uno.                                                            
    - Si se responden 3 preguntas correctamente pasaras al siguiente escalon (asi sucesivamente hasta ganar), de lo contrario perderas.  
    """)          #Reglas del juego
    animales()    #Se llama al primer escalon para dar inicio

if __name__ == "__main__":
    general()