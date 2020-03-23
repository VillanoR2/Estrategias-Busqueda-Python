#Primero construiremosel grafo del mapa, estamos usando el mapa de la ciudad de Rumania y el objetivo es 
#llegar a la ciudad de Bucarest.
#Nosotros nos encontramos en la ciudad de Arad.

grafo = {'Arad':[('Timisoara',118),('Sibiu',140),('Zerind',75)],
        'Timisoara':[('Lugoj',111),('Arad',118)],
        'Sibiu':[('Rimnicu Vilcea',80),('Fagaras',99),('Oradea',151)],
        'Zerind':[('Oraea',71),('Arad',75)],
        'Lugoj':[('Mehadia',70),('Timisoara',111)],
        'Rimnicu Vilcea':[('Pitesti',97),('Craiova',146),('Sibiu',80)],
        'Fagaras':[('Bucarest',211),("Sibiu",99)],
        'Pitesti':[('Bucarest',101),('Timnicu Vilcea',97)],
        'Craiova':[('Pitesti',138),('Dobreta',120),('Rimnicu Vilcea',146)],
        'Mehadia':[('Dobreta',75),('Lugoj',70)],
        'Dobreta':[('Craiova',120),('Mehadia',75)]
        }
        