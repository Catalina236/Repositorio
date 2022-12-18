Number = int(input("Ingrese un número entre 0 y 9.999: "))
if(Number<10):
    print("EL número ingresado tiene una cifra")
elif(Number<100):
        print("El número ingresado tiene dos cifras")
elif(Number<1000):
        print("EL número ingresado tiene tres cifras")
elif(Number<10000):
        print("El número ingresado tiene cuatro cifras")
if (Number>=10000):
    print("Número inválido")
