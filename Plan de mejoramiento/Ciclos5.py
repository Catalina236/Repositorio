i=1
suma=0
print("Introduce una serie de números.Si es 0 entendemos que es para terminar.")
print("Número",i,":",end="")
número=eval(input())
suma=suma+número
while número!=0:
    i=i+1
    print("Número",i,":",end="")
    número=eval(input())
    suma=suma+número
print("La suma de todos los números es",suma)