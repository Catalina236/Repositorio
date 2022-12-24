Número=int(input("Ingrese un número entre 0 y 9.999: "))
if Número<10:
    print("El número ingresado tiene una cifra")
elif Número<100:
    print("El número ingresado tiene dos cifras")
elif Número<1000:
    print("El número ingresado tiene 3 cifras")
elif Número<10000:
    print("El número ingresado tiene 4 cifras")
elif Número>=10000:
    print("Número inválido")
