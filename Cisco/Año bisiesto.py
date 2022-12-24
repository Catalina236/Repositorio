year=int(input("Ingrese año: "))
if year<=1582:
    print("No está dentro del período del calendario gregoriano")
elif year%4!=0:
    print("Es un año común")
else:
    print("Es un año bisiesto")
    