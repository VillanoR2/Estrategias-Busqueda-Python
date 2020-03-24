#Primero construiremos el grafo del mapa, estamos usando el mapa de la ciudad de Rumania y el objetivo es 
#llegar a la ciudad de Bucarest.

grafoB = {'Arad':[('Timisoara',118),('Sibiu',140),('Zerind',75)],
        'Timisoara':[('Lugoj',111),('Arad',118)],
        'Sibiu':[('Rimnicu Vilcea',80),('Fagaras',99),('Oradea',151)],
        'Zerind':[('Oradea',71),('Arad',75)],
        'Lugoj':[('Mehadia',70),('Timisoara',111)],
        'Rimnicu Vilcea':[('Craiova',146),('Pitesti',97),('Sibiu',80)],
        'Fagaras':[('Bucarest',211),("Sibiu",99)],
        'Pitesti':[('Bucarest',101),('Rimnicu Vilcea',97)],
        'Craiova':[('Dobreta',120),('Pitesti',138),('Rimnicu Vilcea',146)],
        'Mehadia':[('Dobreta',75),('Lugoj',70)],
        'Dobreta':[('Craiova',120),('Mehadia',75)],
        'Oradea':[('Zerind',71),('Sibiu',151)],
        'Bucarest':[('Fagaras',211),('Pitesti',101),('Giurgiu',90),('Urziceni',85)],
        'Giurgiu':[('Bucarest',90)],
        'Urziceni':[('Bucarest',85),('Vaslui',142),('Hirsova',98)],
        'Neamt':[('Iasi',87)],
        'Iasi':[('Neamt',87),('Vaslui',92)],
        'Vaslui':[('Iasi',92),('Urziceni',142)],
        'Hirsova':[('Urziceni',98),('Eforie',86)],
        'Eforie':[('Hirsova',86)]
        }

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visitados = [] # List to keep track of visited nodes.
cola = []     #Initialize a queue
camino = []

def bfs(visited, grafo, llave_ciudad, meta):
  visitados.append(llave_ciudad)
  cola.append(llave_ciudad)
  encontrado = False

  while cola and not encontrado:
    nodo_actual = cola.pop(0)
    camino.append(nodo_actual)

    for neighbour,distancia in grafo[nodo_actual]:

      if neighbour not in visited:
         visited.append(neighbour)
         cola.append(neighbour)
      
      if neighbour == meta:
        encontrado = True
        break

    

if __name__ == '__main__':
    bfs(visitados, grafoB, 'Arad','Bucarest')
    print(camino)
    print()

    print(visitados)
