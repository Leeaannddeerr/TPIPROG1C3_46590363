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


