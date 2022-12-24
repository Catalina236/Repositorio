#Imprimir las tablas de multiplicar como el ejercicio antarior pero con for
for i in range(3,7+1):
    print("Tabla del "+str(i))
    for j in range(1,10):
        print(str(i)+"x"+str(j)+"="+str(i*j))