fruta={"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
frut=input("¿Qué fruta desea buscar?: ")
kilos=float(input("¿Cuántos kilos?: "))
if frut in fruta:
    print(fruta.get(frut.title())*kilos)