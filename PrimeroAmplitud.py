from Grafo import Grafo
from Arbol import Arbol


def primero_en_amplitud(grafo, llave_ciudad, meta):
  nodos_visitados = []
  nodos_expandidos = []
  nodos_visitados.append(llave_ciudad)
  nodos_expandidos.append(llave_ciudad)
  encontrado = False
  
  arbol_en_amplitud = Arbol(llave_ciudad)

  while nodos_expandidos and not encontrado:
    nodo_actual = nodos_expandidos.pop(0)
    
    for sucesor,distancia in grafo[nodo_actual]:
      
      if sucesor not in nodos_visitados:
         nodos_visitados.append(sucesor)
         nodos_expandidos.append(sucesor)

         arbol_en_amplitud.añadir(nodo_actual, sucesor)

      if sucesor == meta:
        encontrado = True
        break
  
  return arbol_en_amplitud

if __name__ == "__main__":
    arbol = primero_en_amplitud(Grafo, 'Arad', 'Bucarest')
    arbol.imprimir()