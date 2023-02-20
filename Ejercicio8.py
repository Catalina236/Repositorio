cadena=input("Ingrese una palabra: ")
vocales="aeiou"
vocales_con_tilde="áéíóú"
consonantes="bcdfghjklmnopqrstuvwxyz"
carácteres_especiales="!=$%&/()?¿+*[]{,.}-:;<>|\°¬"
cont=0
for i in cadena:
    if i in vocales:
        cont+=1
cont2=0 
for j in cadena:
    if j in consonantes:
        cont2+=1
cont3=0   
for k in cadena:
    if k in vocales_con_tilde:
        cont3+=1
cont4=0
for l in cadena:
    if l in carácteres_especiales:
        cont4+=1
print("La palabra tiene ",cont,"vocales",cont2,"consonantes",cont3,"vocales con tilde y",cont4,"carácteres especiales.")  