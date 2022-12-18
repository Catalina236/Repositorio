Nombre=input("¿Cómo te llamas?: ")
Edad=int(input("¿Cuántos años tienes?: "))
Dirección=input("Dirección: ")
Teléfono=int(input("¿Cuál es tu número de teléfono?: "))
datos={"Nombre":Nombre,"Edad":Edad,"Dirección":Dirección,"Teléfono":Teléfono}
print(datos["Nombre"],"tiene",Edad,"años, vive en",Dirección,"y su número de teléfono es",Teléfono)