import random
import math 
import networkx as nx
import matplotlib.pyplot as plt



def distance(point1,point2):
    d = math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))
    return d


def close_nodes_points(point,list_points):
    dict_distance = dict()

    for j in range(0,len(list_points)):
        if list_points[j] != point:
            dict_distance[list_points[j]] = distance(point,list_points[j])

    dict_distance = {k: v for k, v in sorted(dict_distance.items(), key=lambda item: item[1])}
    points = [point for point in dict_distance.keys()]
    
    return points


def busca_nodos(lista_puntos,dictNodos):
    nodos_encontrados = []
    for i in range(0,len(lista_puntos)):
        for x,y in dictNodos.items():
            if y == lista_puntos[i]:
                nodos_encontrados.append(x)

    return nodos_encontrados


def search_conexions(node,G):
    nodes_connected = []
    for edge in G.edges:
        if edge[0] == node:
            nodes_connected.append(edge[1])
        elif edge[1] == node:
            nodes_connected.append(edge[0])

    return nodes_connected

def count_conexions_node(node,G):
    list_conexions = search_conexions(node,G)
    #print("count: ",len(list_conexions)," node_start: ",node," conexions: ",list_conexions)
    return len(list_conexions)


def list_new_node_end(list_node,number_condition,G):
    list_end = []
    for node in list_node:
        if count_conexions_node(node,G) < number_condition:
            list_end.append(node)

    return list_end


def validar_conexion(node_start,list_node_end,number_conexions,G):
    if len(search_conexions(node_start,G)) == 0:
        
        list_node_end = list_new_node_end(list_node_end,number_conexions,G)

        return list_node_end[:number_conexions]
    else:
        number_new_conexions = number_conexions - len(search_conexions(node_start,G))
        list_conexions = search_conexions(node_start,G)

        if len(list_conexions) == number_conexions:
            return []

        elif len(list_conexions) != 0:
            for nodo_end in list_node_end:
                for nodo_connected in list_conexions:
                    if nodo_end == nodo_connected:
                        list_node_end.remove(nodo_connected)

        list_node_end = list_new_node_end(list_node_end,number_conexions,G)

        return list_node_end[:number_new_conexions]


def print_conexions(G,list_nodes):
    for node in list_nodes:
        list_conexions = search_conexions(node,G)
        print("count: ",len(list_conexions)," node_start: ",node," conexions: ",list_conexions)


def count_conexions_all_nodes():
    count_edges = []
    for i in range(0, len(G.nodes)):
        count_edges.append(0)

    for edge in G.edges:
        count_edges[edge[0]] += 1
        count_edges[edge[1]] += 1

    return count_edges


"""
main.py
"""


""" Algoritmo de busqueda BFS and Hill-Climbing """

#node_start = int(input("Start node: "))
#node_finish = int(input("Finish node: "))
#option_search_path = int(input("BFS [0]    Hill-CLimbing [1]"))


