#Encontrar la suma y el promedio de los números de la lista.
Lista=[1,2,5,4,8,9,7,6,3,10]
total=0
i=0
for i in Lista:
    total=total+i
print("La suma de",Lista,"es", total)
promedio=total//10
print("El promedio es: ", promedio)