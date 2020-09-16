import networkx as nx
import matplotlib.pyplot as plt


class Node : 
  
    # Utility function to create a new tree node 
    def __init__(self ,key): 
        self.key = key  
        self.child = [] 


class Tree:

    root = None

    def __init__(self):
        root = None

    def find(self,path):
        pass

    def insert(self,path):
        if root == None:
            root.child()




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
      
    # create a queue and enqueue root to it 
    queue = [] 
    queue.append(root) 
  
    # Do level order traversal. Two loops are used 
    # to make sure that different levels are printed 
    # in different lines 
    while(len(queue) >0): 
  
        n = len(queue) 
        while(n > 0) : 
  
            # Dequeue an item from queue and print it 
            p = queue[0] 
            queue.pop(0) 
            print (p.key) 
      
            # Enqueue all children of the dequeued item 
            for index, value in enumerate(p.child): 
                queue.append(value) 
  
            n -= 1
        print() # Seperator between levels 



G = nx.complete_graph(7)
"""
nodo_inicial = 0

root = Node(nodo_inicial)
root_start = root

path = []
list_conexions = search_conexions(nodo_inicial,G)

for nodo in list_conexions:
    root.child.append(Node(nodo))
"""
def generate_tree(G,nodo_inicial,nodo_obj):
    path = []
    level = []

    root = Node(nodo_inicial)

    path.append(root)
    level.append(root)
    
    list_conexions = search_conexions(nodo_inicial,G)

    if len(list_conexions) != 0:
        for nodo in list_conexions:
            root.child.append(Node(nodo))

    root_temp = root
    while len(level) != 0:
        

        
        if len(search_conexions(level))

        for index in range(0,len(root_temp.child)):
            


    return root




path = []

root = Node(0)
root_start = root

path.append(root)

list_conexions = search_conexions(nodo_inicial,G)

if len(list_conexions) != 0:
    for nodo in list_conexions:
        root.child.append(Node(nodo))


root_temp = root_start

root.child.append(Node(1))
root.child.append(Node(2))
root.child.append(Node(3))
root.child.append(Node(4))
root = root_temp.child[0]
root.child.append(Node(5))
root.child.append(Node(6))
root.child.append(Node(7))
root = root_temp.child[0]
root.child.append(Node(5))
root.child.append(Node(6))
root.child.append(Node(7))
root = root_temp.child[1]
root.child.append(Node(5))
root.child.append(Node(6))
root.child.append(Node(7))

printNodeLevelWise(root_start)

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
