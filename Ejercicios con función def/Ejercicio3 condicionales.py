def cifras(número):
    if número<10:
        return "El número ingresado tiene una cifra"
    elif número<100:
        return "El número ingresado tiene dos cifras"
    elif número<1000:
        return "El número ingresado tiene tres cifras"
    elif número<10000:
        return "El número ingresado tiene cuatro cifras"
    else:
        return "Número inválido"
print(cifras(1000))