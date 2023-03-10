from Aprendiz import * #se importa el módulo aprendiz.
from Curso import * #Se importa el módulo de curso.

nombre=input('ingrese nombre del aprendiz') #Se coloca una variable ingresada por teclado.
documento=int(input('ingrese documento del aprendiz'))  #Se coloca una variable ingresada por teclado.
ficha=input('ingrese ficha del aprendiz')  #Se coloca una variable ingresada por teclado.

ap=Aprendiz(ficha,nombre,documento) #Se agrega a una nueva variable que contiene todos los datos.

nombreCurso=input('ingrese nombre del curso') #Se coloca una variable ingresada por teclado que va a tener los nombres de los cursos.
horas=int(input('ingrese intensidad horaria del curso')) #Se coloca una variable ingresada por teclado que va a tener la duración por horas.
c1=Curso(nombreCurso,horas) #Se agregan los datos en una nueva variable.
ap.agregarCurso(c1) #Se añaden con el setter del módulo a una lista.

with open('herencia/aprendices.txt','a') as flujo:    #Se coloca la ruta del archivo al que se van a añadir los módulos y se renombra y se crea un nuevo archivo.
     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n') #Desde esa ruta se colocan las variables que queremos observar en el print concantenándolo con un más.

with open('herencia/aprendices.txt','r') as flujo: #Se coloca la ruta para leer el archivo.
    datos=flujo.read()    #Se coloca una variable para que lea el archivo y lo muestre por pantalla.
    print(datos)
    #flujo.write('2560664,maria,123')
aprendices=[] #Se crea una nueva lista.
with open('herencia/aprendices.txt','r') as flujo: #Se llama nuevamente la ruta con el archivo.
    for linea in flujo: #Se recorre con un ciclo for.
        #print(linea)
        aprendices.append(linea.rsplit()) #Luego se agrega a la lista que se creó anteriormente. 

datosxlinea=[] #Se crea una nueva lista.
for aprendiz in aprendices: #Se recorre la otra lista con un ciclo for.
    datosxlinea.append(aprendiz[0].split(',')) #Se añade a la nueva lista separando los datos que tienen una coma.

#print(ob.getNombre())

print(datosxlinea) #Se imprime la nueva lista.

listaDeObjetos=[] #Se crea otra lista.
for apr in datosxlinea: #Se recorre la anterior con un for.
     f=apr[0] #Se coloca el índice que indica cada elemento que sería el primero para separar cada uno.
     n=apr[1]  #Se coloca el índice que indica cada elemento que sería el primero para separar cada uno.
     d=apr[2]  #Se coloca el índice que indica cada elemento que sería el primero para separar cada uno.
     ob=Aprendiz(f,n,d) #Se coloca en una nueva variable.
     print(ob) #Se imprime.
     listaDeObjetos.append(ob) #Se añaden a la nueva lista.

for xx in listaDeObjetos: #Se recorre con un for.
    print(xx.getNombre()) #Se imprimen los elementos por separado.
    print(xx.getDocumento()) #Se imprimen los elementos por separado.
    print(xx.getFicha()) #Se imprimen los elementos por separado.