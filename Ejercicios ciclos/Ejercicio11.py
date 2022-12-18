a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
cociente=0
if a<b:
    print("No se puede dividir, el primer valor debe ser mayor al segundo")
while a>=b:
    a=a-b
    cociente=cociente+1
print("El resultado es: ", cociente)

