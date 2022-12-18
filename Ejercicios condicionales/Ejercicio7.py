Horas=int(input("Ingrese horas trabajadas: "))
if Horas>40:
    Extras=Horas-40
    Pago=(40*2600)+(Extras*5000)
else:
    Pago=Horas*2600
print("El pago semanal por horas es de $",Pago)
