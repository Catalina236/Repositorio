def edad():#Se define la función sin ningún parámetro..
    try:#Inicio de la excpeción.
        tuedad=int(input("introduce tu edad"))#Se le pide al usuario que ingrese su edad que debe ser un número entero
        print(f'tu edad es {tuedad}')#Se imprime el mensaje "tu edad es",con la edad que ingresó el usuario.
        #print('Tu edad es ',tuedad)
    except ValueError as e:#Excpeción para cuando  el usuario ingresa un dto erróneo:    
        print(e) #Si es así le arrojará el error.
        print("La edad debe ser un valor numerico...")#Con otro mensaje especificando el dato que debe ingresar
        edad()#Es un llamado de la función a ella misma para que se vuelva como un while y pida el número cada vez que ingrese un dato incorrecto.
    
edad()