def nota(número):
    if número<=2:
        return "reprobado"
    elif número<=6:
        return "regular"
    elif número <=8:
        return "sobresaliente"
    elif número <=10:
        return "Excelente"
    else:
        return "El número ingresado es inválido"
print(nota(10))