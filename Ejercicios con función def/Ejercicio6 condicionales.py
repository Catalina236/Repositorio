def Minutos(Num):
    if Num<=3:
        print("El costo de la llamada sería: $", 200)
    if Num>3:
        print("El costo de la llamada sería: $", 200+50*Num-150)
print(Minutos(60))