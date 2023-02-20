alfabeto="abcdefghijklmnopqrstuvwxyz"
palabra=input("Ingrese cualquier palabra: ")
coincidencias=[]
índices=[]
suma=0
for i in palabra:
    if i in alfabeto:
        coincidencias.append(i) 
for letra in coincidencias:
    if letra in alfabeto:
        índices.append(alfabeto.find(letra))
print(índices)
for j in índices:
    suma+=j
print("El valor numérico de",palabra,"según los códigos es: ", suma)