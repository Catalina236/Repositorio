#Encontrar la moda
Lista=[1,2,5,4,8,8,8,8,9,7,3]
repetidos=[]
list=[]
for i in Lista:
        if i not in list:
                list.append(i)
        else:
                repetidos.append(i)
print("La moda es: ", repetidos)