Lista=[1,2,5,4,8,9,7,6,3,10]
swapped=True

while swapped:
    swapped=False
    for i in range(len(Lista)-1):
        if Lista[i]>Lista[i+1]:
            swapped=True
            Lista[i],Lista[i+1]=Lista[i+1],Lista[i]
print(Lista)

swapped=True
while swapped:
    swapped=False
    for i in range(len(Lista)-1):
        if Lista[i]<Lista[i+1]:
            swapped=True
            Lista[i],Lista[i+1]=Lista[i+1],Lista[i]
print(Lista)
Lista=Lista-1

