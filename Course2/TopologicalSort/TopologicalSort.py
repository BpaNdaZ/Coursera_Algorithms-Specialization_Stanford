#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:09:26 2018

@author: BNZ
"""


'''
topological ordering is only possible for a directed acyclic graph(DAG )
(note that if the graph is cyclic then there is no topological order)
any DAG has @ least 1 topological ordering

The key point of using DFS to compute topological order is the sink vertex in a DAG
sink vertices ==> only have incoming edges, no outgoing edges


@ beginning, this algo cannot give the result I want since I had a wrong believe
that all the sink vertices in the original graph must be printed first(see Torder.py)
which is because I perceived the definition of the topological sort in a uncorrected way.


definition: a topological ordering of a DAG is a labeling f(v) of G's v such that
1. f(v)s are the set {1, 2,..., n}, where n is the # of vertices in the DAG
2. if there is an edge (u, v) in the DAG ==> f(u) < f(v)

so with this definition, 1 of the sink points of the original DAG has the len(DAG) label
and all that matters in the topological sort is the order of an edge, that's why
there can be more than 1 topological ordering for a DAG


running time: O(m+n)


'''




# for a directed acyclic graph, careful about the graph you are building
# the sink vertices may not in the graph

'''
think about the data carefully
observe them, find special cases
make sure your read_file reads the data in the right way
'''

def read_file(file_name):
    """
    represent the directed graph as dict[vertex] = [neighbors]
    the sink vertex will be represent as dict[sink_vertex] = []
    key is the vertex
    value is a set contains the connected vertices of that key/vertex
    """
    graph = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip().split(' ')
            if int(line[0]) not in graph:
                graph[int(line[0])] = []
            if int(line[1]) not in graph:
                graph[int(line[1])] = []
            if (int(line[1]) not in graph[int(line[0])]) and (line[0] != line[1]):
                graph[int(line[0])].append(int(line[1]))
          
    return graph



def topologicalOrdering(graph):
    """
    input graph is represented as dict[vertex] = [neighbors]
    compute the order of topological sort using recursive dfs()
    returns the list contains vertices in a topological ordering(from left to right)
    """
    explored = []
    stack = [] #keep the order of the topological sort
    
    for vertex in graph.keys():
    #make sure we search the whole DAG
    #each loop is a dfs branch of the DAG, which will be labeled an topological ordering
        if vertex not in explored: # aggresively dfs the unexplored vertex
            dfs(vertex, graph, explored, stack)
    # after the whole for loop, all branches will be labeled        
    return stack



def dfs(initial_node, graph, explored, stack):
    """
    aggresively explore all the reachable vertices from the initial_node, labeling
    the topological ordering of this branch using a stack
    """
    explored.append(initial_node)
    if len(graph[initial_node]) != 0:
        for neighbor in graph[initial_node]: #this for loop is where the backtrack starts
            if neighbor not in explored:
                explored.append(neighbor)
                dfs(neighbor, graph, explored, stack)
            
    stack.insert(0, initial_node)
    #thanks for the structure of the recursive calls of dfs() itself
    #when the whole for loop finished all the reachable vertices from initial_node
    #have been found and in the stack, so insert initional_node into the stack @
    #the first position ==> f(initial_node) < f(all reachable vertices)



graph = read_file('SCCtest1.txt')
t = topologicalOrdering(graph)
print(t[:13])
















