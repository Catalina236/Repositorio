class lector:
    def __init__(self,nombre,dirección,teléfono):
       self.__nombre=nombre
       self.__direccion=dirección
       self.__teléfono=teléfono
    def verlectores(self):
        return self.__nombre, self.__direccion, self.__teléfono
    
class estudiante(lector):
    def __init__(self,codigo):
        self.__codigo=codigo
    def getcódigo(self):
        return self.__codigo
    def getdato(self,):
        print("Códe:",super().verlectores())

d=estudiante("23456")
print(d.getcódigo())
d.getdato()
class docente(lector):
    def __init__(self,codigodoc):
        self.__codigodoc=codigodoc
    def getcodigodoc(self):
        return self.__codigodoc
    
class pedido(estudiante):
    def __init__(self,título,codigomat,codigo):
        estudiante.__init__(self,codigo)
        self.__título=título
        self.__codigomat=codigomat
    def gettítulocodigo(self):
        return self.__título,self.__codigomat
    def getcod(self):
        print("Código: ",super().getcódigo())