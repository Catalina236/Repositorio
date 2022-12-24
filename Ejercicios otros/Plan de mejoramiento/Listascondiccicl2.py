#Hacer un programa que imprima una lista infinita con los múltiplos de un número ingresado por el usuario.
#Ciclos
Lista=[]
i=1
Num=int(input("Ingrese un número: "))
while Num>0:
    Lista.append(Num*i)
    print(Lista)
    i=i+1