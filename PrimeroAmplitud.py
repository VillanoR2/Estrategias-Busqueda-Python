from Grafo import Grafo
from Arbol import Arbol

nodos_visitados = []
cola = []
arbol = None

def amplitud(visitados, grafo, llave_ciudad, meta):
  visitados.append(llave_ciudad)
  cola.append(llave_ciudad)
  encontrado = False

  ultimo_visitado = llave_ciudad
  global arbol
  arbol = Arbol(ultimo_visitado)

  while cola and not encontrado:
    nodo_actual = cola.pop(0)

    for sucesor,distancia in grafo[nodo_actual]:

      if sucesor not in visitados:
         nodos_visitados.append(sucesor)
         cola.append(sucesor)

         arbol.añadir(ultimo_visitado, sucesor) #añadir al padre del ultimo?
         ultimo_visitado = sucesor

      if sucesor == meta:
        encontrado = True
        break

if __name__ == "__main__":
    amplitud(nodos_visitados, Grafo, 'Arad', 'Bucarest')
    print(nodos_visitados)
    arbol.imprimir()