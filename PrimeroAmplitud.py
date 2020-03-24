from Grafo import Grafo
from Arbol import Arbol

visitados = []
cola = []
arbol = None

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

if __name__ == "__main__":
    #amplitud(visitados, Grafo, 'Arad', 'Bucarest')
    #print(visitados)
    #print()

    a = Arbol('A')
    b = Arbol('B')
    c = Arbol('C')

    b.hijos.append(Arbol('Ba'))
    b.hijos.append(Arbol('Bb'))
    c.hijos.append(Arbol('Ca'))

    a.hijos.append(b)
    a.hijos.append(c)

    arbol_buscado = a.buscar('Bb')
    print(arbol_buscado.valor)

    a.add('Bb','pipo')
    a.add('Bb','pipo2')

    a.add('Ca','nino')

    a.add('pipo2','alex')

    arbol_buscado = a.buscar('pipo')
    print(arbol_buscado.valor)
    print('Impresion del arbol: ')
    a.imprimir()

