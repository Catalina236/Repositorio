values = (1, 0) #Se establecen los valores dentro de una tupla.
#x,y=10,12
#print(divmod(10,3))
try:
    q, r = divmod(*values)#Se establecen los valores de la tupla en una variable y para que los detecte se le coloca el asterisco.
    #print('valor de q=',q)
    print(f'q={q}') #Se imprime el valor que dió la función divmod que en este caso sería el cociente.
    print(f'r={r}')#Se imprime el segundo valor que en este caso sería el residuo.
except (ZeroDivisionError, TypeError) as e: #Estas excpeciones sirven para que en caso tal de que haya un error por división por 0 o un tipo de dato incorrecto se imprimirán sus repectivos mensajes.
    print(type(e), e)