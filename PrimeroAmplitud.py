from Grafo import Grafo
from Arbol import Arbol

visitados = []
cola = []
def amplitud(visitados, grafo, llave_ciudad, meta):
  visitados.append(llave_ciudad)
  cola.append(llave_ciudad)
  encontrado = False

  while cola and not encontrado:
    nodo_actual = cola.pop(0)

    for sucesor,distancia in grafo[nodo_actual]:

      if sucesor not in visitados:
         visitados.append(sucesor)
         cola.append(sucesor)
      if sucesor == meta:
        encontrado = True
        break
