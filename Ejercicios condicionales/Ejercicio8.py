Minutos=int(input("Ingrese el número de minutos gastados: "))
if Minutos<=3:
    print("El costo de la llamada sería: $",200)
if Minutos>3:
    print("El costo de la llamada sería de: $", 200+50*Minutos-150)
