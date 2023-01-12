Valor=int(input("Ingrese cantidad de dinero: "))
if Valor>100000:
    bill=Valor//100000
    print(bill,"billetes de 100000")
    Valor=Valor%100000
if Valor>=50000:
    bill=Valor//50000
    print(bill,"billetes de 50000")
    Valor=Valor%50000
if Valor>=20000:
    bill=Valor//20000
    print(bill,"billetes de 20000")
    Valor=Valor%20000
if Valor>=10000:
    bill=Valor//10000
    print(bill,"billetes de 10000")
    Valor=Valor%10000
if Valor>=5000:
    bill=Valor//5000
    print(bill,"billetes de 5000")
    Valor=Valor%5000
if Valor>=2000:
    bill=Valor//2000
    print(bill,"billetes de 2000")
    Valor=Valor%2000
if Valor>=1000:
    bill=Valor//1000
    print(bill,"billetes de 1000")

