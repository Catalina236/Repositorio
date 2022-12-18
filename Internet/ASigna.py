Asignaturas=["Matemáticas","Física","Química","Inglés","Español"]
Aprobadas=[]
for asignatura in Asignaturas:
    Nota=int(input("Ingrese nota de "+asignatura+":"))
    if Nota>6:
        Aprobadas.append(asignatura)
for asignatura in Aprobadas:
    Asignaturas.remove(asignatura)
print("Tienes que repetir"+str(Asignaturas))
