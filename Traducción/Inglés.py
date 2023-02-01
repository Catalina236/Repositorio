def traducc():
    inglés={"Lápiz":"Pencil","Esfero":"Pen","Regla":"Ruler","Pincel":"Brush","Borrador":"Eraser","Tijeras":"Scissors","Cartuchera":"Pencil case","Colores":"Colors","Notas":"Notes"}
    palabra=input("Ingrese una palabra para traducirla a inglés: ")
    if palabra in inglés:
        return inglés[palabra]
def frances():
    francés={"Lápiz":"Crayon","Esfero":"Sphére","Regla":"Régle","pincel":"Brosse","Borrador":"La gomme","Tijeras":"Paire de ciseaux","Cartuchera":"Poche","Colores":"Colueurs"}
    palabra=input("Ingrese una palabra para traducirla a francés: ")
    if palabra in francés:
        return francés[palabra]