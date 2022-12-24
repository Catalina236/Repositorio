Lista=[1,2,5,4,8,6,9,6,7,7,7,10]
Num=int(input("Ingrese un número: "))
for i in Lista:
    if Num==Lista[i]:
        print("El número",Num, "se ha encontrado en la posición ",[i])
print("Se ha encontrado" ,Lista.count(Num), "veces")

if Num!=Lista:
    Lista.append(Num)
    print(Lista)
