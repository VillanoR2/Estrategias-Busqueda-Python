from Grafo import Grafo
from Arbol import Arbol

def busqueda_en_amplitud(grafo, nodo_inicial, nodo_meta):
    nodos_visitados = []
    cola_de_busqueda = []

    cola_de_busqueda.append(nodo_inicial)

    while cola_de_busqueda:

        nodo_actual = cola_de_busqueda.pop(0) #Se saca el nodo actual

        if nodo_actual not in nodos_visitados: #Si el nodo sacado no se ha visitado, 
            nodos_visitados.append(nodo_actual)
        
        for ciudad, lista_adyacentes in grafo[nodo_actual]:
            if ciudad not in nodos_visitados:
                cola_de_busqueda.append(ciudad)
            
    return nodos_visitados

if __name__ == '__main__':
    #cola_resultado = busqueda_en_amplitud(Grafo,'Arad')
    #print(len(cola_resultado))
    #for nodo in cola_resultado:
    #    print(nodo)
    mi_arbol = Arbol('pipo')
    
    mi_arbol.añadir_hijo('hijo','pipo')

    print(mi_arbol.hijos[0].valor)
    print('done')