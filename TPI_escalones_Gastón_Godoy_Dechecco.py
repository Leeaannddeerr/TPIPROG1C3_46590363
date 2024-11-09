def respuesta(correcta,a,b,c,d):
    print(f"""
    a: {a}        c: {c}
          
    b: {b}        d: {d}
    """)
    usuario = input("Seleccione a, b, c o d: ")
    while "a" != usuario != "b" and "c" != usuario != "d":
        usuario = input("Por favor seleccione a, b, c o d: ")
    if usuario == correcta:
        print("✅ Correcta✅")
        return True
    else:
        print("❌ Incorrecta❌")
        return False

def siguiente_escalon():
    if animales() >= 3:
        if geografia() >= 3:
            if historia() >= 3:
                if entretenimiento() >= 3:
                    aleatorias()

def seguir(cont):
    if cont >= 3:
        print("Felicitaciones, pasaste al siguiente escalon 🎉")
        print(f"Respondiste bien {cont}!")
    else:
        print("No pasas al siguiente escalon :(")
        print(f"Respondiste bien {cont} preguntas")
        usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        while "si" != usuario != "no":
            usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        if usuario == "si":
            general()
        else:
            print("Gracias por jugar!")

def animales():
    contador = 0
    print("Bienvenido al escalon de animales 🐾")
    print("1) ¿Qué animal es famoso por su habilidad de hacerse el muerto?")
    if respuesta("a","Zarigüeya", "Conejo", "Zorro", "Buho"):
        contador += 1
    print("2) ¿Cuáles son los únicos felinos que viven en grupos?")
    if respuesta("d","Tigres", "Pumas", "Leopardos", "Leones"):
        contador += 1
    print("3) ¿Qué animal tiene el cerebro más grande?")
    if respuesta("b","Elefante", "Cachalote", "Delfin", "Calamar"):
        contador += 1
    print("4) ¿Qué mamífero africano es conocido particularmente por su risa?")
    if respuesta("d","Zebra", "Jirafa", "Avestruz", "Hiena"):
        contador += 1
    print("5) ¿Cuantas patas tiene una araña?")
    if respuesta("c","4", "6", "8", "10"):
        contador += 1
    seguir(contador)
    return contador

def geografia():
    contador = 0
    print("Bienvenido al escalon de geografia 🌎")
    print("1) ¿Cuántos océanos hay en la Tierra?")
    if respuesta("c","2", "3", "5", "8"):
        contador += 1
    print("2) ¿En qué país se encuentra la famosa torre de Pisa?")
    if respuesta("a","Italia", "Francia", "España", "Estados unidos"):
        contador += 1
    print("3) ¿Cual es el país más grande del mundo?")
    if respuesta("a","Rusia", "China", "India", "Brasil"):
        contador += 1
    print("4) ¿Cuál es la montaña más alta del mundo?")
    if respuesta("b","Aconcagua", "Monte everest", "Manaslu", "Makalu"):
        contador += 1
    print("5)  ¿Cuál es la lengua más hablada del mundo?")
    if respuesta("d","Español", "Mandarin", "Portugues", "Ingles"):
        contador += 1
    seguir(contador)
    return contador

def historia():
    contador = 0
    print("Bienvenido al escalon de historia 📜")
    print("1) ¿Cómo se llamaban los gobernantes del antiguo Egipto?")
    if respuesta("b","Reyes", "Faraones", "Dioses", "Alcaldes"):
        contador += 1
    print("2) Según las leyendas de la antiguedad, ¿quiénes fundaron a Roma?")
    if respuesta("c","Aquiles y Odiseo", "Alejandro magno y Ptolomeo", "Rómulo y Remo", "Aquiles y Perseo"):
        contador += 1
    print("3) Los samuráis eran:")
    if respuesta("c","Antiguos guerreros persa", "Aliados de los espartanos", "Antiguos guerreros japoneses", "Cazarrecompensas"):
        contador += 1
    print("4) El dios sol en la cultura inca se llamaba:")
    if respuesta("c", "Quetzalcóatl", "Huitzilopochtli", "Inti", "Quilca"):
        contador += 1
    print("5)  ¿Con qué nombre se conoce la crisis económica generada por el crac financiero de Wall Street en 1929?")
    if respuesta("a","La gran depresion", "El plan marshall", "La crisis del golfo", "Ninguna"):
        contador += 1
    seguir(contador)
    return contador

def entretenimiento():
    contador = 0
    print("Bienvenido al escalon de entretenimiento 🕹️")
    print("1) ¿Cuál es la fruta favorita de los minions?")
    if respuesta("d","Papas", "Frutillas", "Zanahorias", "Bananas"):
        contador += 1
    print("2) ¿De qué color es la G mayúscula en el logotipo de Google?")
    if respuesta("c","Roja", "Amarilla", "Azul", "Verde"):
        contador += 1
    print("3)  Las Tortugas Ninja se llaman Leonardo, Donatello, Michelangelo ¿y...‍")
    if respuesta("b","Doraemon", "Raphael", "Rumachello", "Miguel"):
        contador += 1
    print("4) En la era del hielo, ¿quien era scrat? El animal que persigue la bellota")
    if respuesta("a","Ardilla", "Nutria", "Marmota", "Zorro"):
        contador += 1
    print("5)  ¿Cual es el juego mas vendido del mundo?")
    if respuesta("d","Grand Theft Auto V", "Tetris", "Pac-Man", "Minecraft"):
        contador += 1
    seguir(contador)
    return contador

def aleatorias():
    contador = 0
    print("Bienvenido al escalon de preguntas aleatorias 🎲")
    print("1) ¿a que temperatura hierve el agua (grados celcius)?")
    if respuesta("b","90°", "100°", "120°", "200°"):
        contador += 1
    print("2) ¿Qué país ha ganado más Copas del Mundo?")
    if respuesta("c","Argentina", "Francia", "Brasil", "Alemania"):
        contador += 1
    print("3)  ¿Qué vitamina fabrica el propio cuerpo usando la luz del sol?")
    if respuesta("b","Vitamina C", "Vitamina D", "Vitamina A", "Vitamina E"):
        contador += 1
    print("4) ¿Cuántos fantasmas persiguen a Pac-Man al principio de cada partida?")
    if respuesta("a","4", "6", "8", "1"):
        contador += 1
    print("5)  ¿Cuál es el animal nacional de Australia?")
    if respuesta("d","Condor", "Flamenco", "Lagartija", "Canguro"):
        contador += 1
    if contador >= 3:
        print("🎊 Felicitaciones, ganaste el juego 🎊")
        print(f"Respondiste bien {contador} preguntas")
        usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        while "si" != usuario != "no":
            usuario = input("¿Desea reintentar el juego? (si o no)").lower()
        if usuario == "si":
            general()
        else:
            print("Gracias por jugar!")

def general():
    print("Bienvenido a los 5 escalones")
    print("""
    Reglas del juego:
    - Son 5 escalones, cada escalon es una tematica diferente y tienen 5 preguntas cada uno.
    - Si se responden 3 preguntas correctamente pasaras al siguiente escalon (asi sucesivamente hasta ganar), de lo contrario perderas.
    """)
    siguiente_escalon()

if __name__ == "__main__":
    general()