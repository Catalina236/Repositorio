#Múltiplos comprendidos entre 5 y N
N=int(input("Ingrese un número: "))
for i in range(1,N):
    if i%5==0:
      print(i)