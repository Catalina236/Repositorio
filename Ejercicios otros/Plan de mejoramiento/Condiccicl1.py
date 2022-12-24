#Números primos hasta n:
n=int(input("Introduce un número: "))
for i in range(2,n+1):
    cont=0
    for j in range(1,n+1):
        if i%j==0:
            cont+=1
    if cont==2:
        print(i)