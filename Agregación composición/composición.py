class Curso: #Se crea un objeto.
    def __init__(self,titulo): #Se crea el constructor.
        self.__titulo=titulo #Se instancia.

    def getTitulo(self): #Se crea una función para obtener el nombre del curso.
        return self.__titulo #Se retorna

class Aprendiz: #Se crea otro objeto llamado Aprendiz
    def __init__(self,nombre): #Se crea el constructor.
        self.__nombre=nombre #Se instancia.
        self.__cursos=[] #Se crea una lista privada.

    def agregarCurso(self,nombreCursito): #Se crea una función para añadir los cursos
        cursito=Curso(nombreCursito) #Se instancia
        self.__cursos.append(cursito) #se añade a la lista.

    def getCursos(self): #Se crea un getter para obtener los elementos de la lista.
        return self.__cursos
    
ap=Aprendiz('Sofia') #Se añaden los parámetros.
ap.agregarCurso('Python Basico') 
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos(): #Se recorre la lista de cursos.
    print(c.getTitulo()) #Se imprime el getter para visualizar los cursos

del ap #Se borra el elemento Aprendiz