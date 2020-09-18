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

    print("...arbol de estados generando")

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
                """
                for i in range(0,len(path)):
                    print("camino fuera bucle: ",path[i].key)
                print()
                """

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
 
            ### Si hay nodos conectados para insertar ###

            else:
     
                for nodo in list_conexions:
                    root_temp.child.append(Node(nodo))
                
                path.append(root_temp.child[0])
                level.append(root_temp.child[0])

                root_temp = root_temp.child[0]

    
    return root


def busqueda_amplitud(G,nodo_inicial,nodo_objetivo):
    
    tree_root = generate_tree(G,nodo_inicial)
    
    print("...buscando el mejor camino")
    root_tmp = tree_root

    print_queue = []

    queue = []
    camino = []
    queue.append([tree_root.key,camino,tree_root])
    print_queue.append([tree_root.key,camino])

    while True:
        #print("cola caminos: ",print_queue)

        if len(queue) == 0:
            return False

        elif queue[0][0] == nodo_objetivo:
            queue[0][1].append(nodo_objetivo)
            return queue[0][1]
        
        else:
            
            path = []
            if len(queue[0][1]) == 0:
                path.append(queue[0][0])

            else:
                path = queue[0][1].copy()
                path.append(queue[0][0])

            root_tmp = queue[0][2]

            queue.pop(0)
            print_queue.pop(0)
            
            for i in range(0,len(root_tmp.child)):
                queue.append([root_tmp.child[i].key,path,root_tmp.child[i]])
                print_queue.append([root_tmp.child[i].key,path])

        

