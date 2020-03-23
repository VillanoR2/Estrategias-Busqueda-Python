from Grafo import Grafo

def busqueda_en_amplitud(grafo, nodo_inicial):
    nodos_visitados = []
    cola_de_busqueda = []

    cola_de_busqueda.append(nodo_inicial)

    while cola_de_busqueda:
        nodo_actual = cola_de_busqueda.pop(0)
        if nodo_actual not in nodos_visitados:
            nodos_visitados.append(nodo_actual)
        
        for ciudad, lista_sucesores in grafo[nodo_actual]:
            if ciudad not in nodos_visitados:
                cola_de_busqueda.append(ciudad)
            
    return cola_de_busqueda

if __name__ == '__main__':

    a = busqueda_en_amplitud(Grafo,'Arad')

