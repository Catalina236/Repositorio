print("Menú:\n 1.Para buscar una canción\n 2.Para agregar una canción si no está en la lista.\n 3.Para agregar artistas \n Para salir presiona enter")
#Para buscar una canción:
artista2=["Metallica","Burning Witches","Crypta","Judas Priest"]
canciones=["Enter Sandman","Hexenhammer","From the ashes","Burn in hell"]
artista=input("¿Qué artista desea buscar?: ")
if artista not in artista2:
    print("No se encuentra en la lista")
    artista2.append(artista)
else:
    print("Se encuentra en la lista")
canción=input("¿Qué canción desea buscar?: ")
if canción not in canciones:
    print("No se encuentra en la lista, pero se arega a sus favoritos. Si gusta, puede seguir dándonos información de la canción")
    canciones.append(canción)
else:
    print("Se encuentra en la lista")
canciones_artistas={}
for i in range(len(artista2)):
    canciones_artistas[artista2[i]]=canciones[i]
canciones_sort=sorted(canciones_artistas.items())
print(canciones_sort)

    