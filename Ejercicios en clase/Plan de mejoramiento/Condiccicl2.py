#Página 71  Libro python fácil
#Hacer un programa que determine si un número es primo.
#Ciclos
Num=int(input("Ingrese un número: "))
cont=0
for i in range(1,Num+1):
     if Num%i==0:
      cont=cont+1
if cont>2:
      print(Num,"no es primo")
else:
    print(Num,"es un número primo")