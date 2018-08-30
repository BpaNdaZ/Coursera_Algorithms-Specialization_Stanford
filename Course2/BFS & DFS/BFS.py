# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:46:57 2018

@author: BNZ
"""


'''
breath first search needs a initial node and will explore the undirected graph by "layer"

after we run the breath first search, all the nodes we explored are reachable
from the initial node and also reaschable from each other (undirected graph)

since BFS explore the graph by "layer" it can be used to solve the problem
<shortest path from s to t> by keep tracking every node's layer

BFS also can be used in undirected connectivity to node s problem

running time is O(n_s + m_s)
n_s is the # of nodes reachable from s
m_s is the edges reachable from s

'''

# implementation
# there will be a FIFO queue Q to simulate the procedure of exploring the graph by layers
# we dequeue the 1st node in the Q and put all of its unexplored neighbors into Q --> FIFO
# and mark those neighbors as explored



import queue

def breathFirstsearch(graph, initial_node):
    """
    input graph is represented as dic[node] =[neighbors]
    initial_node is where we start to explore the graph
    return the reachable nodes from initial_node
    """
    explored_nodes = [initial_node]
    # except the initial node, all nodes are marked as unexplored
    q = queue.Queue()
    q.put(initial_node)

    while not q.empty():
        dequeue_node = q.get()
        # remove the node whose neighbors were explored from Q

        for i in graph[dequeue_node]:
            # scan all of the neighbors of the dequeued node
            if i not in explored_nodes:
                # put unexplored neighbors into Q and marked as explored
                explored_nodes.append(i) # mark explored
                q.put(i)
                
    return explored_nodes



def read_file(file_name):
    """
    represent the graph as a dictionary
    key is the vertix
    value is a list contains the connected vertices of that key/vertix
    """
    graph = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip().split(' ')
            graph[int(line[0])] = [int(x) for x in line[1:]]
            
    return graph
    


graph = read_file('test1.txt')
explored_nodes = breathFirstsearch(graph, 1)
print(explored_nodes)










