#Un número es perfecto si la suma de sus divisores es igual a este, sin incluir el mismo
n=int(input("Ingrese número: "))
i=1
total=0
while (i<n):
    if n%i==0:
        total=total+i
    i=i+1
if total==n:
 print(n,"Es un número perfecto")
else:
 print(n,"No es un número perfecto")

