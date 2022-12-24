Minutos=int(input("Ingrese minutos gastados: "))
if Minutos<=3:
    print(Minutos*200)
elif Minutos>3:
    Banderazo=Minutos-3
    Gasto=Banderazo*50
    Tarifa=3*200+Gasto
    print(Tarifa)
