class Persona:#Se asigna una clase llamada persona con la palabra class
    def __init__(self,nombre): #Esta línea funciona para referenciar el contenido del objeto.
        self.__nombre=nombre  #Las dos líneas se usan para volver privado el parámetro

        #print('Constructor Activado')        

    def getNombre(self): #Esta línea es para crear una función que servirá para acceder al nombre o parámetro que definimos como privado.
        return self.__nombre #Esta línea retorna el valor.
    
    def setNombre(self,nombre): #Esta línea es para crear una función que añadirá otro nombre al parámetro.
        self.__nombre=nombre #Esta línea añade el nombre al parámetro.

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())