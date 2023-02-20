palabra=input("Ingrese un verbo: ")
dosúltimas=palabra[-2:]
tresúltimas=palabra[-3:]
cincoúltimas=palabra[-5:]
acento="áéíóú"
def tiempopasado():
    if dosúltimas in "rérá" or tresúltimas in "rásrán" or cincoúltimas in "remos":
        print("Futuro")
    elif dosúltimas in "do":
        print("Pasado participio")
    elif tresúltimas in "ronice" or palabra[-4:] in "iste" or palabra[-1] in acento:
        print("Pasado")
    else:
        print("Presente") 
tiempopasado()