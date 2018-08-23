# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:22:47 2018

@author: BNZ
"""


def read_file(file_name = 'kargerMinCut.txt'):
    """
    represent the graph as a dictionary
    key is the vertix
    value is a list contains the connected vertices of that key/vertix
    """
    graph = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip().split('\t')
            graph[int(line[0])] = [int(x) for x in line[1:]]
            
    return graph


def buildEdgeContainer(graph):
    """
    build an edge container from the graph
    each edge in this container is represented by a set
    since {1,2} and {2,1} represent the same edge, only one of them will be in the container
    return the edge container
    """
    edges = []
    candidates = []
    for vertix, neighbors in graph.items():
        candidates.extend({vertix, x} for x in neighbors)
    for i in candidates:
        if i not in edges:
            edges.append(i)
            
    # initially there is no multiedge in edges
    # but we should change & maintain this container in a way that allows multigraph
    
    # change to list representation
    edges_list = [list(edge) for edge in edges]
            
    return edges_list





import random

def randomEdge(edges):
    """
    truely random pick an edge from the container uniformly and return it
    """
    random.shuffle(edges)
    random_edge = random.choice(edges)
    
    return random_edge




def mantainedgescontainer(edges, u, v):
    """
    multigraph arises during the edge contraction
    maintain edges from contracted multigraph
    """
    for i in edges.copy():
        if v in i:
            a = i.copy()
            edges.remove(i)
            a[i.index(v)] = u
            edges.append(a)
    # when there is loops
    for i in edges.copy():
        if i[0] == i[1]:
            edges.remove(i)
            
    return edges
        
    
    
    


def kargerMinCut(graph):
    """
    here even though the edge is really uniformly random picked, however, the running \
    time is almost 1 min...
    
    need to think this through later
    
    """
    edges = buildEdgeContainer(graph)
    
    while len(graph) > 2:
        
        '''
        how to build an edge container from the graph???
        for vertice, neighbors in graph.items():
            
        '''
        
        u, v = randomEdge(edges)
        edges.remove([u, v])
        edges = mantainedgescontainer(edges, u, v)
        
        '''
        random_node = random.choice(list(graph.keys()))
        random_edge = random.choice(graph[random_node])
        u, v = random_node, random_edge
       '''
        
        # edge contraction in the graph
        
        # merge 2 vertices u,v as a single vertix u in the graph
        # remove the edge in the graph
        if v in graph[u]:
            graph[u].remove(v)
        if u in graph[v]:
            graph[v].remove(u)
        
        # attach all v's neighbors to u's neighbors
        graph[u].extend(graph[v])
        
        # change all the v in v's neighbors' neighbors list to u
        for i in graph[v]:
            while v in graph[i]:
                graph[i].remove(v)
                graph[i].append(u)
        
        # delete the vertix v in the graph_copy
        del graph[v]
        
        # delete the loops arised from contraction
        # loop can be found by checking u's updated neighbors
        # do not iterating a list while changing it, use copy or while
        while u in graph[u]:
                graph[u].remove(u)
                
        cut = list(graph.values())
        
    return len(cut[0])
        
        
graph= read_file()
# print(graph)

# edge = randomEdge(edges)
# print(edge)

import copy
import time

start = time.time()
min_cut = 500
for i in range(101):
    graph_file = copy.deepcopy(graph)
    cut = kargerMinCut(graph_file)
    if cut < min_cut:
        min_cut = cut
    else:
        continue

print(min_cut)
print(time.time() - start)
    


