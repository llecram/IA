import random
import math 
import networkx as nx
import matplotlib.pyplot as plt

import graph 
import state_tree as st_tree
import samplePoints as spoint

"""Iniciando programa"""

G = nx.Graph()
num_nodes = int(input("Number of nodes: "))
num_conexions = int(input("Number conexions: "))


""" Generando nodos aleatorios que no repiten posicion """

G.add_nodes_from(range(0,num_nodes))

pos_good = spoint.get_good_points(num_nodes,4)
print("len: ",len(pos_good))

pos = dict()
i=0
while len(pos) < num_nodes:
    xpos = pos_good[i][0] #random.randint(0,300)
    ypos = pos_good[i][1] #random.randint(0,300)
    
    if (xpos,ypos) not in pos.values():
        pos[i] = (xpos,ypos)
        i+=1


""" Conectando nodos a nodos mas cercanos """

list_node_start = [node for node in pos]
list_points = [point for point in pos.values()]


for i in range(0,len(list_node_start)):
    list_node_edges = graph.close_nodes_points(list_points[i],list_points)

    lista_node_end = graph.busca_nodos(list_node_edges,pos)

    """ revisar nodos con muchas conexiones y cero conexiones"""
    lista_node_end = graph.validar_conexion(list_node_start[i],lista_node_end,num_conexions,G)

    #evaluar para no hacer doble enlace

    for j in range(0,len(lista_node_end)):
        G.add_edge(list_node_start[i],lista_node_end[j])


edges_reverse = []

for edge in G.edges:
    edges_reverse.append((edge[1],edge[0]))

for edge in G.edges:
    for j in range(0,len(edges_reverse)):
        if edge == edges_reverse[j]:
            G.remove_edge(edges_reverse[j])


""" revisar nodos con muchas conexiones y cero conexiones"""

for nodo in G.nodes:
    print("nodo: ",nodo," cant conx: ",graph.count_conexions_node(nodo,G))




nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)

labels = {}
for i in range(0,num_nodes):
    labels[i] = i

nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.show()

""" Busqueda amplitud """

nodo_inicio = int(input("nodo inicial: "))
nodo_objetivo = int(input("nodo objetivo: "))



camino_found = st_tree.busqueda_amplitud(G,nodo_inicio,nodo_objetivo)


if camino_found == False:
    print("No se encontro camino")
    print()

else:
    print("camino encontrado: ",camino_found)
    print()

    camino_edges = []
    j=0
    for i in range(0,len(camino_found)):
        j += 1
        edge_tmp = (camino_found[i],camino_found[j])
        camino_edges.append(edge_tmp)

        if j==len(camino_found)-1:
            break

    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_nodes(G,pos,nodelist = camino_found,node_color="green")
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_edges(G,pos,edgelist=camino_edges,edge_color="r")

    labels = {}
    for i in range(0,num_nodes):
        labels[i] = i

    nx.draw_networkx_labels(G,pos,labels,font_size=12)

    plt.show()