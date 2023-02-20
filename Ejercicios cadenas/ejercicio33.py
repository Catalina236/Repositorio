palabra=input("Ingrese una palabra: ")
código=[]
suma=0
for letra in palabra:
    código.append(ord(letra))  
for j in código:
    suma+=j    
print("El valor numérico de los códigos es: ",suma)