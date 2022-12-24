import random
def parimpar(num):
    if num%2==0:
        print("par")
    else:
        print("impar")
Lista=[]
for i in range(10):
    Lista.append(round(random.randrange(100)))
print(Lista)
for i in Lista:
    print(i)
    parimpar(i)
    