Asignaturas=["Matemáticas","Física","Química","Inglés","Español"]
Nota=[]
for i in Asignaturas:
    note=input("¿Cuánto se sacó el estudiante en "+i+"?: ")
    Nota.append(note)
for j in range(len(Asignaturas)):
    print("En",Asignaturas[j],"has sacado:",Nota[j])
