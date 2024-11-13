import re
#funcion para separar la palabra en silabas 
def separar_silabas(palabra):
    silabas = []
    palabra = palabra.lower()
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
    return silabas

def jeringoso(palabra):#recibe palabra y convierte en jeringoso
    jeringosa = '' #cadena que almacena
    vocales = ('a', 'e', 'i', 'o', 'u')#tupla de vocales
    silabas = separar_silabas(palabra) #separar la palabra en silabas

    silaba_anterior = '' #variable para almacenar la silaba anterior

    for i in range(len(silabas)):
        silaba = silabas[i]
        silaba_jeringosa = '' #cadena para la silaba convertida a jeringoso

        for j in range(len(silaba)):
            letra = silaba [j]
            if letra.lower()in vocales:
                if j == len(silaba) -1 and silaba_anterior:
                    silaba_jeringosa += 'p'+ silaba_anterior[-1]
                else:
                    silaba_jeringosa += letra
            else: 
                silaba_jeringosa += letra
    jeringosa += silaba_jeringosa

    silaba_anterior = silaba

    return jeringosa

def main():#menu
     diccionario = {} #diccionario vacio para almacenar las palabras y las versiones de jeringoso
     while True:#pide la palabra, verifica si es salir, y si no lo es lo convierte a jeringoso la palabra
          print("\nMenu de opciones:")
          print("1. Ingresar una palabra") 
          print("2. Mostrar historial de palabras en jeringoso")
          print("3. Salir") 
          opcion = input("Elige una de las siguientes opciones (1, 2, o 3):").strip()
          if opcion == "1":  # Opción para ingresar una palabra
            palabra = input("Ingresa una palabra: ").strip()
            palabra_jeringosa = jeringoso(palabra)
            diccionario[palabra] = palabra_jeringosa  # Guardar la palabra y su versión en jeringoso
            print(f"Palabra en jeringoso: {palabra_jeringosa}")
          elif opcion == "2": 
            if diccionario: 
                print("\nHistorial de palabras en jeringoso: ")
                for palabra, palabra_jeringosa in diccionario.items():
                  print(palabra,"-->",palabra_jeringosa)
            else:
                print("No se han ingresado palabras") 
          elif opcion == "3":
              print("Gracias! Hasta la próxima")
              break
          else:
              print("Opción no válida. Por favor ingrese una opción válida (1, 2, o 3)")
        
if __name__ == "__main__":
    main()
