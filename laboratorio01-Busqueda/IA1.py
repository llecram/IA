import networkx as nx
import matplotlib.pyplot as plt
import math
import threading, queue
import random

def hb(g,ni,nf):
    ni1=g.nodes[ni]
    nf1=g.nodes[nf]
    ne=neightbours(g,ni1)#ordenar de menor a mayor con respecto a su distancia con el nodo final
    path=deque()
    while(1):
        if(len(ne)==0):
            ne.pop(0);
            path.pop()
        if(ne[0]==nf1):
            path.append(ne[0])
            break
        else:
            ne1=neightbours(g,ne[0])#ordenar de menor a mayor con respecto a su distancia con el nodo final
            path.append(ne[0])
            ne.pop(0)            
            for i in ne1:
                ne.insert(ne1[i])

Grafo = nx.Graph()
n_nodos = 10
n_conexiones = 5
lengthss={}
distancia_nodo_objetivo={}
for i in range (0,n_nodos):
    Grafo.add_node(i,pos=(random.randint(0,100),random.randint(0,100)),value = i)
    
for i in range (0, n_nodos):
    for j in range(0, n_nodos):
        if i != j:
            lengthss[j]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[j]['pos'][1])**2)+((Grafo.nodes[j]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))
        length_sort={k: v for k, v in sorted(lengthss.items(), key=lambda item: item[1])}
        #print (length_sort)
    for h in range(0,n_conexiones):
        Grafo.add_edge(i,next(iter(length_sort)))
        next(iter(length_sort))
        length_sort.pop(list(length_sort.keys())[0])
    lengthss ={}
#print(Grafo.edges())
for i in range(0,n_nodos):
    if i != n_nodos-1:
        distancia_nodo_objetivo[i]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[n_nodos-1]['pos'][1])**2)+((Grafo.nodes[n_nodos-1]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))

#print (distancia_nodo_objetivo)

Arbol_sol=nx.Graph()
Arbol_sol.add_node(0,pos =(0,0),value=0)
x = 1
for i in range(0,n_nodos):
    for edge in Grafo.edges([i]):
        #Arbol_sol.add_node(x,value=edge[1])
        #startnode = Arbol_sol.nodes[0]
        #endnode = Arbol_sol.add_node(x,value=edge[1])
        Arbol_sol.add_node(x,value=edge[1])
        #print(Arbol_sol.nodes[x]['value'])
        Arbol_sol.add_edge(i,x)
        x = x + 1
diction={}
for i in range(0,len(Arbol_sol)):
    diction[i] = str(Arbol_sol.nodes[i]['value'])
print (diction)
#mapping={k: v for k, v in sorted(diction.items(), key = lambda item: item[1])}
Arbol = nx.relabel_nodes(Arbol_sol, diction)
#print(Grafo.edges())
pos=nx.get_node_attributes(Grafo,'pos')
#nx.draw(Grafo,pos,with_labels=True)
#plt.show()
print(Grafo.edges())
print(Arbol_sol.nodes())
nx.draw(Arbol,with_labels=True)
plt.show()