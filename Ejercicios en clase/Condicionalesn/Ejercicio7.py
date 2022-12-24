Horas=int(input("Ingrese horas trabajadas: "))
if Horas<=40:
    print(Horas*2600)
elif Horas>40:
    Salar=40*2600
    SalarioHo=Horas-40
    Salario=SalarioHo*5000+Salar
    print(Salario)