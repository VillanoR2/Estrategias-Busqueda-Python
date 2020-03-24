class Arbol:
    def __init__(self,valor):
        self.hijos = []
        self.valor = valor

    def añadir_hijo(self, valor, valorPadre):
        arbol_padre = buscar_subarbol(self, valorPadre)
        arbol_padre.hijos.append(Arbol(valor))

def buscar_subarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol

    for hijo in arbol.hijos:
          arbol_buscado = buscar_subarbol(hijo, valor)
          if (arbol_buscado != None):
             return arbol_buscado
        
     return None
        