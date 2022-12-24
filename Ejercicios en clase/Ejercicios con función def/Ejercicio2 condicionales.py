def Iguales(a,b,c):
    if a==b and a==c and b==c:
        return "Los 3 son iguales"
    elif a==b or a==c or b==c:
        return "Hay dos números idénticos."
    else:
        return "Todos son diferentes."
a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
print(Iguales(a,b,c))
    