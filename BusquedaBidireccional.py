from Arbol import Arbol
from Grafo import Grafo


def busqueda_bidireccional(inicio, meta, grafo):
    #Listas de nodos expandidos
    busqueda_adelante = []
    busqueda_reversa = []
    busqueda_adelante.append(inicio)
    busqueda_reversa.append(meta)

    #Listas nodos visitados
    visitados_adelante = []
    visitados_adelante.append(inicio)
    visitados_reversa = []
    visitados_reversa.append(meta)

    #Arboles de ambas busquedas
    arbol_adelante = Arbol(inicio, [inicio])
    arbol_reversa = Arbol(meta, [meta])

    se_interceptan = False
    nodo_interceptado = None

    while (busqueda_adelante or busqueda_reversa) and not se_interceptan:
        nodo_actual = busqueda_adelante.pop(0)
        
        for sucesor, distancia in grafo[nodo_actual]:
            if sucesor not in visitados_adelante:
                visitados_adelante.append(sucesor)
                busqueda_adelante.append(sucesor)

                arbol_adelante.añadir(nodo_actual, sucesor)

            if sucesor in busqueda_reversa:
                se_interceptan = True
                nodo_interceptado = sucesor
                break


        nodo_actual = busqueda_reversa.pop(0)    
        for sucesor,distancia in grafo[nodo_actual]:
            if sucesor not in visitados_reversa:
                visitados_reversa.append(sucesor)
                busqueda_reversa.append(sucesor)
                arbol_reversa.añadir(nodo_actual, sucesor)

            if sucesor in busqueda_adelante:
                se_interceptan = True
                nodo_interceptado = sucesor
                break

    camino_mas_corto = arbol_adelante.buscar(nodo_interceptado).camino
    listaAux = arbol_reversa.buscar(nodo_interceptado).camino
    listaAux.reverse()
    print('Arbol de la busqueda desde el inicio:')
    arbol_adelante.imprimir()
    print('\nÁrbol de la búsqueda desde la meta:')
    arbol_reversa.imprimir()
    camino_mas_corto.extend(listaAux)
    return camino_mas_corto




if __name__ == "__main__":
    print('\n\n')
    camino = busqueda_bidireccional('Arad', 'Bucarest', Grafo)
    print('\nCamino mas corto por búsqueda bidireccional: ')
    print(camino)
