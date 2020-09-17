import random
import math 
import networkx as nx
import matplotlib.pyplot as plt

import graph 
import state_tree as st_tree


"""Iniciando programa"""

G = nx.Graph()
num_nodes = int(input("Number of nodes: "))
num_conexions = int(input("Number conexions: "))


""" Generando nodos aleatorios que no repiten posicion """

G.add_nodes_from(range(0,num_nodes))

pos = dict()
i=0
while len(pos) < num_nodes:
    xpos = random.randint(0,100)
    ypos = random.randint(0,100)
    
    if (xpos,ypos) not in pos.values():
        pos[i] = (xpos,ypos)
        i+=1

""" Conectando nodos a nodos mas cercanos """

list_node_start = [node for node in pos]
list_points = [point for point in pos.values()]


for i in range(0,len(list_node_start)):
    list_node_edges = graph.close_nodes_points(list_points[i],list_points)
    lista_node_end = graph.busca_nodos(list_node_edges,pos)

    lista_node_end = graph.validar_conexion(list_node_start[i],lista_node_end,random.randint(1,num_conexions),G)

    #evaluar para no hacer doble enlace

    for j in range(0,len(lista_node_end)):
        G.add_edge(list_node_start[i],lista_node_end[j])



nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)

labels = {}
for i in range(0,num_nodes):
    labels[i] = i

nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.show()


nodo_inicio = int(input("nodo inicial: "))
nodo_objetivo = int(input("nodo objetivo: "))

""" Busqueda amplitud """

camino_found = st_tree.busqueda_amplitud(G,nodo_inicio,nodo_objetivo)

if camino_found == False:
    print("No se encontro camino")
    print()
    
else:
    print("camino encontrado: ",camino_found)
    print()
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_nodes(G,pos,nodelist = camino_found,node_color="green")
    nx.draw_networkx_edges(G,pos)

    labels = {}
    for i in range(0,num_nodes):
        labels[i] = i

    nx.draw_networkx_labels(G,pos,labels,font_size=12)

    plt.show()