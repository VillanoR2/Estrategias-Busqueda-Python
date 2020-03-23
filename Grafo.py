#Primero construiremos el grafo del mapa, estamos usando el mapa de la ciudad de Rumania y el objetivo es 
#llegar a la ciudad de Bucarest.

Grafo = {'Arad':[('Timisoara',118),('Sibiu',140),('Zerind',75)],
        'Timisoara':[('Lugoj',111),('Arad',118)],
        'Sibiu':[('Rimnicu Vilcea',80),('Fagaras',99),('Oradea',151)],
        'Zerind':[('Oradea',71),('Arad',75)],
        'Lugoj':[('Mehadia',70),('Timisoara',111)],
        'Rimnicu Vilcea':[('Pitesti',97),('Craiova',146),('Sibiu',80)],
        'Fagaras':[('Bucarest',211),("Sibiu",99)],
        'Pitesti':[('Bucarest',101),('Rimnicu Vilcea',97)],
        'Craiova':[('Pitesti',138),('Dobreta',120),('Rimnicu Vilcea',146)],
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