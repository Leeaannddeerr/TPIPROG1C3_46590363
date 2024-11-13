def jeringoso(palabra):#recibe palabra y convierte en jeringoso
    jeringosa = ''
    vocales = ('a', 'e', 'i', 'o', 'u')#tupla de vocales
    for i in range(len(palabra)):#for para recorrer, si la letra es vocal agrega p seguido de la vocal
        letra=palabra[i]
        if letra.lower() in vocales:
            jeringosa+="p"+letra
        else:
            jeringosa+=letra
    return jeringosa


def main():#maneja la interaccion con el usuario
     diccionario= {} #diccionario vacio para almacenar las palabras y las versiones de jeringoso
     while True:#pide la palabra, verifica si es sair, y si no lo es lo convierte a jeringoso la palabra
          palabra=input("Ingresa una palabra o escribe salir para terminar: ")
          if palabra.lower()== "salir":
               break
          palabra_jeringosa=jeringoso(palabra)
          diccionario[palabra]=palabra_jeringosa
          print("Palabra en jeringoso:",palabra_jeringosa)
print("Diccionario de palabras en jeringoso:")

<<<<<<< HEAD
=======
if __name__ == "__main__":
    main()
>>>>>>> 34d36be4a8e1972afc4d81a4750a95b0969b4ff0
