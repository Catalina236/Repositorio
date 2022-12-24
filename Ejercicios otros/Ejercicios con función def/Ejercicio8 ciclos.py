#Determinar cuáles son los múltiplos de 5 comprendidos entre 1 y N
def múltiplos(N):
    for i in range(1,N+1):
        if i%5==0:
            print(i)
múltiplos(45)
