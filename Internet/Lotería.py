Lotería=[]
Número=int(input("Ingrese los números ganadores: "))
while Número>0:
    if Número!=0:
        Lotería.append(Número)
    Número=int(input("Ingrese los números ganadores: "))
Lotería.sort()
print("Los números ganadores son", Lotería)