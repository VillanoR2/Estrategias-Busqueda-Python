from Grafo import Grafo
from Arbol import Arbol

nodos_visitados = []
nodos_expandidos = []
arbol = None

def amplitud(visitados, grafo, llave_ciudad, meta):
  visitados.append(llave_ciudad)
  nodos_expandidos.append(llave_ciudad)
  encontrado = False
  
  global arbol
  arbol = Arbol(llave_ciudad)

  while nodos_expandidos and not encontrado:
    nodo_actual = nodos_expandidos.pop(0)
    print('Nodo actual: ' + nodo_actual)

    for sucesor,distancia in grafo[nodo_actual]:
      
      if sucesor not in visitados:
         nodos_visitados.append(sucesor)
         nodos_expandidos.append(sucesor)

         arbol.añadir(nodo_actual, sucesor)

      if sucesor == meta:
        encontrado = True
        break

if __name__ == "__main__":
    amplitud(nodos_visitados, Grafo, 'Arad', 'Bucarest')
    print(nodos_visitados)
    arbol.imprimir()