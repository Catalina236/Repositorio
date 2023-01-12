import math
Ángulo=int(input("Ingrese ángulo: "))
A=float(Ángulo)
A1=math.radians(A)
cos=(math.cos(A1))
sen=math.sin(A1)
tan=math.tan(A1)
if sen>0 and cos>0:
    print("Primer cuadrante")
if sen>0 and cos<0:
    print("Segundo cuadrante")
if sen<0 and tan>0:
    print("Tercer cuadrante")
if cos>0 and tan<0:
    print("Cuarto cuadrante")
print("Está en la",Ángulo//360,"vuelta")
print(A1,"radianes")

