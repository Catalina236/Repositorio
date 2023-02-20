palabra=input("Ingrese una palabra: ")
def aguda():
    última_letra=palabra[-1]
    if última_letra in "áéíóúns":
        print("Es aguda")
    else:
        print("No es aguda.")        
aguda()
def grave():
    #palabra=input("Ingrese una palabra: ")
    última_letra=palabra[-1]
    dos_últimas=palabra[-2:]
    for letra in palabra:
        if letra in "áéíóú" and última_letra in "aeiounsáéíóú" and dos_últimas not in "psíads":
            print("No es grave")
            break
        elif letra in "áéíóú" and dos_últimas in "psdsía":
                print("Es grave")
                break
    else:
        print("Es grave.")
grave()        

def esdrújula():
    palabra=input("Ingrese una palabra: ")
    vocales = "aeiouáéíóúüsmr"
    acento="áéíóú"
    silabas = []
    silaba_actual = ""
    for i, letra in enumerate(palabra):
        silaba_actual += letra
        if letra in vocales:
            if i == len(palabra) - 1:
                silabas.append(silaba_actual)
            elif palabra[i+1] not in vocales:
                silabas.append(silaba_actual)
                silaba_actual = ""
        
    try:
        antepenúltima=silabas[-3]
        for j in palabra:
                if palabra.endswith("mente") and j in antepenúltima:
                    print("No es esdrújula")
                    break
                if palabra.endswith("mente") and j not in acento:
                    print("Sí es esdrújula")
                    break
                if j in antepenúltima and not palabra.endswith("mente"):
                    print("Sí es esdrújula")
                    break
    except IndexError:
        print("No es esdrújula al tener poca cantidad de sílabas.")            
    print(silabas)
esdrújula()

def sobreesdrújula():
    palabra=input("Ingrese una palabra: ")
    ulti3=palabra[-3:]
    ulti5=palabra[-5:]
    for letter in palabra:
        if len(palabra)>6 and ulti3 in "elo" or ulti5 in "mente" and letter in "áéíóú":
            print("Es sobreesdrújula")
            break
    else:
        print("No es sobreesdrújula")        
sobreesdrújula()        