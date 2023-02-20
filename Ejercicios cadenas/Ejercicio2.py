palabra=input("Ingrese una palabra: ")
for i in range(len(palabra)):
    for j in range(i):
        i+=j
print("El valor de la suma de todos los códigos de la palabra es: ",i)