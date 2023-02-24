def divisores(num): #Definimos una función
    try:      #Try funciona para indicar el bloque de código que se va a probar si llega a haber algún error en el bloque.
        for i in range(num+1): #Empezamos a recorrer el ciclo hasta llegar al número
            if num%i==0:
                print(i,' es divisor') #Si el residuo da un valor de 0, se va a imprimir el número que indica que es un divisor del número ingresado.
    except ZeroDivisionError: #Se coloca la excepción ZeroDivisionError para que arroje un mensaje que indique que la división no se puede realizar si el divisor es igual 0
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')#Esta línea sirve para que el usuario ingrese los datos correctos al momento de dividir.
var=int(input('ingrese numero'))#Se le pedirá al usuario ingresar un número entero
divisores(var) #Se llama la función.
print('El programa continua en esta linea')#Es para que cuando haya un error imprima la excepción y este mensaje.