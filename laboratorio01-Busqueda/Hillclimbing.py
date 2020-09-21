import networkx as nx
import matplotlib.pyplot as plt
import math
import threading, queue
import random
def get_key(val): 
    for key, value in dist_neighbors.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"
Grafo = nx.Graph()
print("Ingrese el numero de nodos: ")
n_nodos=int(input())
print("\n Ingrese el numero de conexiones: ")
n_conexiones=int(input())
print("\n Ingrese el nodo inicial: ")
nodo_ini=int(input())
print("\n Ingrese el nodo objetivo: ")
nodo_objetivo=int(input())
lengthss={}
path_find = False
distancia_nodo_objetivo={}
for i in range (0,n_nodos):
    Grafo.add_node(i,pos=(random.randint(0,100),random.randint(0,100)),value = i, n_edges = 0, path = False)
    
for i in range (0, n_nodos):
    for j in range(0, n_nodos):
        if i != j:
            lengthss[j]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[j]['pos'][1])**2)+((Grafo.nodes[j]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))
        length_sort={k: v for k, v in sorted(lengthss.items(), key=lambda item: item[1])}
    for h in range(0, n_conexiones):
       for g in list(length_sort):
           if Grafo.nodes[i]['n_edges'] < n_conexiones and Grafo.nodes[next(iter(length_sort))]['n_edges'] < n_conexiones :
               Grafo.add_edge(i,next(iter(length_sort)))
               Grafo.nodes[i]['n_edges'] +=1
               Grafo.nodes[next(iter(length_sort))]['n_edges'] +=1
           length_sort.pop(list(length_sort.keys())[0])
    lengthss = {}

for i in range(0,n_nodos):
    if i != n_nodos:
        distancia_nodo_objetivo[i]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[nodo_objetivo]['pos'][1])**2)+((Grafo.nodes[nodo_objetivo]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))


nodo_inicial = nodo_ini
nodo_final = nodo_objetivo
nodo_cam = Grafo.nodes[nodo_inicial]
i = 0
path = []
path.append(nodo_inicial)
while nodo_cam['value'] != nodo_final:
    dist_neighbors = {}
    menor = 0
    key = 0
    hijo = 0
    for edges in Grafo.edges([nodo_cam['value']]):
        hijo = edges[1]
        if (Grafo.nodes[hijo]['path'] != True):
            dist_neighbors[hijo]=distancia_nodo_objetivo[hijo]
            if (hijo == nodo_final or distancia_nodo_objetivo[hijo] == 0 ):
                menor = distancia_nodo_objetivo[hijo]
                break
            if menor == 0:
                menor = distancia_nodo_objetivo[hijo]
            if distancia_nodo_objetivo[hijo] < menor and distancia_nodo_objetivo[hijo] != 0 and nodo_cam['path']!= True:
                menor = distancia_nodo_objetivo[hijo]
    key = get_key(menor)
    if key == "key doesn't exist":
        print ("Camino no encontrado")
        path_find = False
        break
    else:
        path_find = True
    path.append(key)
    nodo_cam['path']=True
    nodo_cam = Grafo.nodes[key]
    Grafo.nodes[nodo_inicial]['path'] = True    
Grafo.nodes[nodo_final]['path'] = True
color_map = []
for i in range (0,n_nodos):
    if Grafo.nodes[i]['path'] == True :
        color_map.append('red')
    else:
        color_map.append('green')    

if path_find:
    print ("Camino encontrado: ",path)
    pos=nx.get_node_attributes(Grafo,'pos')
    nx.draw(Grafo,pos, node_color = color_map,with_labels=True)
    plt.show()
