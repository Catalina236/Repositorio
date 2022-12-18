#Obtener los divisores del número ingresado
numero = int(input("Ingrese el número: "))
print("Los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0:
     print(divisor)