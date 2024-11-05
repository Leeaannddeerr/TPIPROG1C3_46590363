def jeringoso(palabra):
    jeringosa = ''
    vocales = ('a', 'e', 'i', 'o', 'u')
    for i in range(len(palabra)):
        letra=palabra[i]
        if letra.lower() in vocales:
            jeringosa+="p"+letra
        else:
            jeringosa+=letra
    return jeringosa


def main():
     diccionario= {}
     while True:
          palabra=input("Ingresa una palabra o escribe salir para terminar: ")
          if palabra.lower()== salir:
               break
          palabra_jeringosa=jeringoso(palabra)
          diccionario[palabra]=palabra_jeringosa
          print("Palabra en jeringoso:",palabra_jeringosa)
print("Diccionario de palabras en jeringoso:")