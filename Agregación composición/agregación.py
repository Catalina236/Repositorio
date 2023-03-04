class Aprendiz: #Se crea el objeto.
    def __init__(self,nombre): #Se crea el constructor.
        self.__nombre=nombre # Se crea la instancia.
        self.__cursos=[] #Se crea una lista privada
    def agregarCurso(self,nombreCurso): # Se crea una función que servirá para añadir el curso.
        self.__cursos.append(nombreCurso) #Se usa el método append para añadir los cursos a la lista.
    def verCursos(self): #se crea un método para ver la lista.
        return self.__cursos #Retorna los cursos de la lista.

class Curso: #Se crea el siguiente objeto.
    def __init__(self,nombreCurso): #Se crea el constructor.
        self.__nombreCurso=nombreCurso #Se crea la instancia que será privada.

    def getNombreCurso(self): #Se crea un método para obtener el nombre del curso.
        return self.__nombreCurso #Se usa un return para que retorne el nombre.
    
ob=Aprendiz('Miguel') #Se añaden los parámetros.
c1=Curso('Python Basico')
c2=Curso('Python Intermedio')
c3=Curso('Java Basico')

ob.agregarCurso(c1)  #Se llama la función con los parámetros.
ob.agregarCurso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos(): #Se recorre la lista.
    print(curso.getNombreCurso()) #Se immprime la lista 

del ob #Se borra la clase aprendiz
#print(ob)
print('.....',c1.getNombreCurso())  #Se imprime el nombre de los cursos.