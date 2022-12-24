canciones={}
Menú=input("Menú:\n1.Para buscar o añadir una canción con su artista.\n2.Para mostrar lista.\nEnter para salir del menú: ")
while Menú!="":
    if Menú=="1":
        canción=input("Ingresa la canción que deseas buscar: ")
        if canción not in canciones:
            Artista=input("La canción no se encuentra ¿De qué artista es?: ")
            print("La canción se añadió a su lista de favoritos.")
            if Artista not in canciones:
                canciones.setdefault(canción,Artista)
        canciones_sort=sorted(canciones.items())
    elif Menú=="2":
        print(canciones_sort)
    Menú=input("Menú:\n1.Para buscar o añadir una canción con su artista.\n2.Para mostrar lista.\nEnter para salir del menú: ")
