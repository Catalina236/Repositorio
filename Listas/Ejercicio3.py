#Sumar los números pares y sacar el promedio de los impares.
Lista=[1,2,5,4,8,9,7,6,3,10]
par=0
impar=0
impar=impar+1
for i in Lista:
    if i%2==0:
        par=par+i
    if i%2!=0:
        impar=impar+i/10
print("La suma de los números pares es:", par)
print("El promedio de los números impares es: ",impar)