import Menu
#funcion para separar la palabra en silabas 
def separar_silabas(palabra):
    silabas = []
    palabra = palabra.lower() #convierte la palabra a minusculas
    vocales = "aeiou"
    silaba = ""
   
    for i in range(len(palabra)): #itera sobre la palabra usando indices
        letra = palabra[i] #a partir del indice se accede a la letra 
        silaba += letra #agrega la letra a la silaba temporal

        if letra in vocales:
            if i + 1 < len(palabra) and palabra[i + 1] not in vocales:
                silabas.append(silaba) #agrega la silaba a la lista
                silaba = "" #resetea la variable
            elif i + 1 ==len(palabra): #si estamos en la ultima letra de la palabra
                silabas.append(silaba) #agrega la ultima silaba
    if silaba:
        silabas.append(silaba)
    return silabas #devuelve la lista de silabas

def jeringoso(palabra):#recibe palabra y convierte en jeringoso
    jeringosa = '' #cadena que almacena
    vocales = ('a', 'e', 'i', 'o', 'u')#tupla de vocales
   
    silaba_anterior = '' #variable para almacenar la silaba anterior

    for i in range(len(palabra)):
        letra = palabra[i]
    

        if letra.lower()in vocales:
            jeringosa +=  letra + 'p' + letra #se agrega la letra, seguida de p y despues de nuevo por la letra
        else:
            jeringosa += letra #si no es vocal, solo se agrega a la cadena
                 
    return jeringosa #devuelve la palabra convertida a jeringoso

def main():#menu
     diccionario = {} #diccionario vacio para almacenar las palabras y las versiones de jeringoso
     while True:#pide la palabra, verifica si es salir, y si no lo es lo convierte a jeringoso la palabra
          print("\nMenu de opciones:📖")
          print("1. Ingresar una palabra ✍🏼") 
          print("2. Mostrar historial de palabras en jeringoso 📚")
          print("3. Volver al menú de juegos")
          opcion = input("Elige una de las siguientes opciones (1, 2, o 3): ").strip() #pide al usuario una opcion y elimina los espacios en blanco al inicio y final
          if opcion == "1":  # Opción para ingresar una palabra
            palabra = input("Ingresa una palabra: ").strip()
            palabra_jeringosa = jeringoso(palabra)
            diccionario[palabra] = palabra_jeringosa  # Guardar la palabra y su versión en jeringoso
            print("Palabra en jeringoso:",palabra_jeringosa)
          elif opcion == "2": 
            if diccionario: 
                print("\nHistorial de palabras en jeringoso: ")
                for palabra, palabra_jeringosa in diccionario.items():
                  print(palabra," ➡️➡️➡️ ",palabra_jeringosa)
            else:
                print("No se han ingresado palabras") 
          elif opcion == "3":
              print("Gracias! Hasta la próxima👋🏼", Menu.menu()) #te devuelve al menu principal de los juegos
              break
          else:
              print("Opción no válida. Por favor ingrese una opción válida (1, 2, 3, o 4)")
        
if __name__ == "__main__":
    main()
