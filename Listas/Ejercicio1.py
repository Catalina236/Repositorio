#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo del promedio o es igual al promedio de todos los números de la lista.
Lista=[1,2,5,4,8,9,7,6,3,10]
suma=0
i=0
promedio=0
for i in Lista:
    suma=suma+i
    promedio=suma//10
print("El promedio es: ", promedio)
for i in Lista:
    if i>promedio:
            print("El número",i,"está por encima del promedio.")
    if i<promedio:
            print("El número",i,"está por debajo del promedio.")
    if i==promedio:
            print("El número",i,"es igual al promedio.")