a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
if a<b:
    while b>0:
        r=a%b
        a=b
        b=r
    print(a)
elif a>b:
    print("No se puede hallar el mcd")