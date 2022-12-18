def ubicación(Num):
    for i in range(len(Lista)):
        if Num==Lista[i]:
            print("El elemento",Num,"se ha encontrado en la posición: ",[i])
    print("Se ha encontrado",Lista.count(Num),"veces")
    if Num!=Lista:
            Lista.append(Num)
Lista=[1,2,5,4,8,6,9,6,7,7,7,10]
print(ubicación(6))
print(Lista)
