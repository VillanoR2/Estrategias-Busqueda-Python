class Arbol:
    def __init__(self,valor):
        self.hijos = []
        self.valor = valor

    def imprimir(self, nivel = 1):
        i = 1
        while i < nivel:
            print('\t', end = '')
            i = i +1
        
        print(self.valor)

        for hijo in self.hijos:
            hijo.imprimir(nivel + 1)


    def añadir(self, valor_padre, valor_hijo):
        padre = self.buscar(valor_padre)
        padre.hijos.append(Arbol(valor_hijo))

    def buscar(self, valor_buscado):
        return buscarF(self, valor_buscado)


def buscarF(arbol, valor_buscado):
    if (arbol.valor == valor_buscado):
        return arbol
    else:
        for hijo in arbol.hijos:
            
            resultado = buscarF(hijo, valor_buscado)
            if (resultado is not None):
                return resultado
            
    return None