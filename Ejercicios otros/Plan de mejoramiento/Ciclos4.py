#Imprimir las tablas de multiplicar de los números pares.
for i in range(2,10,2):
    print("Tabla del "+str(i))
    for j in range(1,10+1):
        print(str(i)+"x"+str(j)+"="+str(i*j))