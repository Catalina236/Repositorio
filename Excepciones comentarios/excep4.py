def try_syntax(numerator, denominator):#Se define la función con dos parámetros.
    try:#Acá inicia la excepción
        print(f'In the try block: {numerator}/{denominator}')
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator #acá se asigna una variable para el resultado de la división
    except ZeroDivisionError as zde: #Acá se renombra la excepción
        print(zde)
    else:
        print('The result is:', result) #Esta línea es para que cuando no haya ningún error se imprima el resultado.
        return result
    finally: #Esta línea sirve para finalizar el código cuando no tiene errores.
        print('Exiting')
        return "Fallo por zero"
print(try_syntax(12, 4))
#print(try_syntax(11, 'a'))