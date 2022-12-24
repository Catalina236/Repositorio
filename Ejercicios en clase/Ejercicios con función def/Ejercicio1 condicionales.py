def Valor_medio(a,b,c):
    if a<b<c:
        return "El valor medio es: ",b
    elif b<a<c:
        return "El valor medio es: ",a
    elif b<c<a:
        return "El valor medio es: ",c
    elif a<b>c:
        return "El valor medio es: ",c
    elif a>b>c:
        return "El valor medio es: ",b
print(Valor_medio(2,3,11))