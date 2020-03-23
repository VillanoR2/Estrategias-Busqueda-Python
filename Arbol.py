class Arbol:
    def __init__(self,valor):
        self.hijos = []
        self.valor = valor

    def añadir_hijo(self, valor, valorPadre):
        subarbol = buscarSubarbol(self, valorPadre)
        subarbol.hijos.append(Arbol(valor))

    def buscarSubarbol(self, elemento):
        if self.elemento == elemento:
            return self

        for hijo in self.hijos:
            arbolBuscado = buscarSubarbol(hijo, valor)
            if (arbolBuscado != None):
                return arbolBuscado
        
        return None
        