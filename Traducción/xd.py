palabras = ["Lápiz", "Esfero", "Regla","Pincel","Borrador","Tijeras","Cartuchera","Colores","Notas"]
categoria = "sustantivo"
tipo_palabra = {}

for palabra in palabras:
        tipo_palabra[palabra] = categoria
word=input("Ingrese una palabra: ")
if word in tipo_palabra:
    print(tipo_palabra[word])
    