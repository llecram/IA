import networkx as nx
import matplotlib.pyplot as plt


class Node : 

    def __init__(self ,key): 
        self.key = key  
        self.child = [] 


def search_conexions(node,G):
    nodes_connected = []
    for edge in G.edges:
        if edge[0] == node:
            nodes_connected.append(edge[1])
        elif edge[1] == node:
            nodes_connected.append(edge[0])

    return nodes_connected



def printNodeLevelWise(root): 
    if root is None: 
        return 

    queue = [] 
    queue.append(root) 
  
    while(len(queue) >0): 
  
        n = len(queue) 
        while(n > 0) : 
  
            p = queue[0] 
            queue.pop(0) 
            print (p.key) 

            for index, value in enumerate(p.child): 
                queue.append(value) 
  
            n -= 1
        print()



G = nx.Graph()
G.add_nodes_from(range(1,7))
G.add_edge(0,6)
G.add_edge(0,3)
G.add_edge(0,5)
G.add_edge(0,4)
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,5)
G.add_edge(2,4)
G.add_edge(5,4)
G.add_edge(5,6)

def buscar_nodo(camino,raiz):

    root_temp = raiz

    if len(camino) == 1:
        return raiz

    i=1
    while i < len(camino):   
        e=0
        while e < len(root_temp.child):
            if camino[i] == root_temp.child[e]:
                root_temp = root_temp.child[e]
                
            e +=1
        
        i += 1

    return root_temp


def generate_tree(G,nodo_inicial):
    path = []
    level = []

    root = Node(nodo_inicial)

    path.append(root)
    level.append(root)
    
    root_temp = root

    while len(path) != 0:
        
        if len(level) == 0:
            break

        ### Verfica conexiones de nodo actual ####
        
        list_conexions = search_conexions(level.pop().key,G)

        ### Verifica que existan conexiones ###

        if len(list_conexions) != 0:
            
            ### Si hay mas nodos se borran los nodos conectados que estan presentes en el camino y asi evitar bucles ###

            if len(path)-1 != 0:
                
                ### Evita que cuente el nodo actual y asi evite ciclo del mismo nodo ###
                
                for i in range(0,len(path)):  ### len(path)-1 antes
                    for nodo in list_conexions:
                        if nodo == path[i].key:
                            list_conexions.remove(nodo)          

            ### Si no hay nodos conectados para insertar ###

            if len(list_conexions) == 0:
                
                for i in range(0,len(path)):
                    print("camino fuera bucle: ",path[i].key)
                print()

                level.append(path.pop())
                
                ### retorna nodo padre del nodo actual ###
                
                root_temp = buscar_nodo(path,root)
                
                subida = False
    
                while True:
                    
                    for i in range(0,len(root_temp.child)):
                        ### Evalua que el nodo padre solo tenga un hijo para buscar padre de ese nodo ###

                        if i+1 == len(root_temp.child):
                            subida = True
                            break     
                        
                        ### Evalua que el nodo padre tenga mas hijos para trabajar con nodo hijo siguiente ###

                        elif root_temp.child[i] == level[0]:

                            path.append(root_temp.child[i+1])
                            level.pop()
                            level.append(root_temp.child[i+1])
                            root_temp = root_temp.child[i+1]
                            subida = False
                            break

                    ### Se busca un nuevo nodo padre ###

                    if subida == True:

                        level.pop()
                        level.append(path.pop())

                        if len(path) == 0:
                            subida = False
                            break         

                        root_temp = buscar_nodo(path,root)

                    ### Ya se trabaja con el nodo con el flujo normal ###

                    elif subida == False:
                        break
 
                print("sali del bucle while padre")

            ### Si hay nodos conectados para insertar ###

            else:
                print("nodo crea hijos: ",root_temp.key)
                for nodo in list_conexions:
                    root_temp.child.append(Node(nodo))
                
                path.append(root_temp.child[0])
                level.append(root_temp.child[0])

                root_temp = root_temp.child[0]


    return root



tree_root = generate_tree(G,0)



"""
nodo_inicial = 0

list_conexions = search_conexions(nodo_inicial,G)

queue = []
queue.append(nodo_inicial)
list_conexions = search_conexions(nodo_inicial,G)

queue.pop(0)
path = []
path.append(list_conexions[0])
path.append(nodo_inicial)
queue.append(path)
path.clear()

def busqueda_amplitud(nodo_inicial,nodo_objetivo,G):
    pass

"""

"""
nx.draw(G,with_labels=True)
plt.show()
"""
