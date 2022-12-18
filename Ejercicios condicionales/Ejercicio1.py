Num1=int(input("Ingrese el primer número: "))
Num2=int(input("Ingrese el segundo número: ")) 
Num3=int(input("Ingrese el tercer número: "))
if Num1<Num2<Num3:
   print("EL valor del medio es: ",Num2)
elif Num2<Num1<Num3:
   print("El valor del medio es: ",Num1)
elif Num2<Num3<Num1:
  print("El valor del medio es: ",Num3)
elif Num1<Num2>Num3:
  print("El valor del medio es: ",Num3)
elif Num1>Num2<Num3:
  print("El valor del medio es: ",Num2)
elif Num1>Num2>Num3:
  print("EL valor del medio es: ",Num2)
elif Num1<Num2>Num3:
  print("El valor del medio es: ",Num1)
else:
  print("El valor del medio es:",Num2)

