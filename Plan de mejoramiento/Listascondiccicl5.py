# Página 282  Libro python fácil
#Investigue y programe el algoritmo de ordenación Bubble Sort(ordenamiento burbuja)
# Listas
Lista=[2,3,9,5,10,51,23,65,90,110,85]
swapped=True
while swapped:
    swapped=False
    for i in range(len(Lista)-1):
        if Lista[i]>Lista[i+1]:
            swapped=True
            Lista[i],Lista[i+1]=Lista[i+1],Lista[i]
print(Lista)