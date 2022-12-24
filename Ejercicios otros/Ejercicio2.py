Num=int(input("Ingrese un número: "))
print("El opuesto es: ", Num*-1)
conter=1
while Num!=0:
   Num=int(input("Ingrese un número diferente a cero: "))
   conter=conter+1
   print("El opuesto es:", Num*-1)
else:
   print("El valor de números ingresados es: ",conter)
