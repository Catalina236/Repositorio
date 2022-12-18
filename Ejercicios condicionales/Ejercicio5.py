print("Responda sí o no a las preguntas, gana quién responda correctamente las 3 preguntas. Si se responde mal a cualquiera, ya no se pregunta la siguiente y termina el juego. Las preguntas son: ")
print("1. ¿Colón descubrió América?: ")
Respuesta=str(input(""))
if Respuesta=="si":
    print("2. ¿La independencia de Colombia fue en el año 1810?")
else:
    print("Incorreto, has perdido el juego.")
Respuesta=str(input(""))
if Respuesta=="si":
    print("3. ¿The Doors fue un grupo de rock americano?")
else:
    print("Incorrecto, has perdido el juego.")
Respuesta=str(input(""))
if Respuesta=="si":
    print("Felicidades, has ganado el juego.")
else:
    print("Incorrecto,has perdido el juego.")
