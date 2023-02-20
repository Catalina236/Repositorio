alfabeto="abcdefghijklmnopqrstuvwxyz"
palabra="comedor"
repetidas=0
cont=0
resta=0
adición=0
for j in palabra:
    cont+=1
for k in palabra:    
    if palabra.count(k)>1:
        repetidas+=1
        resta=cont-repetidas
        adición=resta+1
print("La palabra tiene",adición,"letras sin repeticiones")
alfabeto="abcdefghijklmnopqrstuvwxyz"
palabra="comedor"
letras_únicas=set(palabra)
print(len(letras_únicas))