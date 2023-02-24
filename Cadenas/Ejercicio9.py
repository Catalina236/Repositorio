palabra=input("Ingrese una palabra: ").lower()
cifrado={"v":0,"e":1,"n":2,"t":3,"i":4,"l":5,"a":6,"d":7,"o":8,"r":9}
for i in palabra:
    if cifrado==i.replace(a,b):
        print(cifrado[i],end="")
    else:
        print(i,end="")