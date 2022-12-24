Lista=[1,2,5,4,8,9,7,6,3,10]
Número=1
while Número<=len(Lista):
    x=1
    Contador=0
    while x<=Número:
        if Número%x==0:
            Contador=Contador+1
        x=x+1
    if Contador==2:
        print("El número", Número, "es primo")
    Número=Número+1
print("Hay", Contador, "números primos en la lista")