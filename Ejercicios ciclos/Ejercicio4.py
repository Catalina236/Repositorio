#Hay solo 3 numeros perfectos inferiores a 1000
n=1
cont=0
for n in range(1,1000):
    total = 0
    for j in range(1,n):
        if n%j == 0:
            total += j
        if total == n:
            cont=cont+1
            print(n)
            break
print("Hay",cont,"números perfectos")
    
        