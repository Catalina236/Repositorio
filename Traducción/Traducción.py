inglés={}
español=['Maleta', 'Cuaderno', 'Pegante', 'Lápiz', 'Crayolas', 'Tijeras', 'Regla', 'Borrador', 'Resaltador', 'Esfero', 'Transportador', 'Cartuchera', 'Marcador', 'Tajalápiz', 'Carpeta', 'Notas', 'Calculadora', 'Colores', 'Corrector', 'Compás', 'Diccionario', 'Pincel']
vi=['Bag', 'Notebook', 'Glue', 'Pencil', 'Crayons,', 'Scissors', 'Ruler', 'Eraser', 'Highlehter pen', 'Pen', 'Conveyor', 'Pencil case', 'Marker', 'Sharpener', 'Folder', 'Sticky notes', 'Calculator', 'Colors', 'Concealer', 'Compass', 'Dictionary', 'Brush']
franc=["Valise","Cahier","Colle","Crayon","Des crayons","paire de ciseaux","Régle","La gomme","surligneur","Sphére","Convoyeur","Poche","Marqueur","Taille-crayon","Dossier","Remarques","Calculatrice","Couleurs","Correcteur","Le compas","Dictionnaire","Brosse"]
francés={}
for i in range(len(español)):
    inglés[español[i]]=vi[i]
for j in range(len(español)):
    francés[español[j]]=franc[j]
tipo_palabra={}
tipo="sustantivo"
for l in español:
    tipo_palabra[l]=tipo
def búsqueda():
    buscar=input("Ingrese la palabra que desea traducir: ").lower()
    for k in [inglés,francés,tipo_palabra]:
        for key in k.keys():
            if key.lower()==buscar:
                return "Inglés:"+inglés[key]+"\nFrancés:"+francés[key]
        else:
            return "No se encuentra."
def palabra():
    word=input("Ingrese una palabra: ").lower()
    for key in tipo_palabra.keys():
        if key.lower()==word:
            return word+" es un "+tipo_palabra[key]
    else:
        return "No se encuentra."