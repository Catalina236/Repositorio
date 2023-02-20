alfabeto="abcdefghijklmnopqrstuvwxyz"
coincidencias=[]
índices=[]
def sumacódigos():
    palabra=input("Ingrese cualquier palabra: ")
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

código=[]
def sumacod():
    palabra=input("Ingrese una palabra: ")
    suma=0
    for letra in palabra:
        código.append(ord(letra))  
    for j in código:
        suma+=j    
    print("El valor numérico de los códigos es: ",suma)
sumacod()    