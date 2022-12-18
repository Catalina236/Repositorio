# Ingresar 3 números y ver cuántos son iguales
a = int(input("Ingrese un número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
if(a==b)and(a==c)and(b==c):
        print("Los tres números son iguales")
else:
    if(a==b)or(a==c)or(b==c):
      print("Hay dos números iguales")
    elif(a!=b):
        print("Los tres números son distintos")
