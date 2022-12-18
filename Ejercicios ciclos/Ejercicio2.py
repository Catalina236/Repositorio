n=int(input("Ingrese un número:"))
esprimo=True
for i in range(2,n):
    if n%i==0:
        esprimo=False
        break
if esprimo:
     print(n,"Es un número primo")
else:
     print(n,"No es un número primo")
