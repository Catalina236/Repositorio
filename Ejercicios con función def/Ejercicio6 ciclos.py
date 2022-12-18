def números(a):
    c=0
    while a>0:
        a=int(input("Ingrese un número: "))
        if a>0:
            c=c+1
        if a<=0:
            print("El máximo de números ingresados es: ",c)
(números(1))