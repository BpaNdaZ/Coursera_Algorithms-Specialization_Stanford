#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:52:57 2018

@author: BNZ
"""


'''
topological ordering is only possible for a DAG --> directed acyclic graph
any DAG has 2 least 1 topological ordering

The key point of using DFS to compute topological order is the sink vertex in a 
directed acyclic graph.(note that if the graph is cyclic then there is no topological order)
sink vertices ==> only have incoming edges, no outgoing edges

do sink vertices should be included in the graph.keys()?


during the DFS, we will agressively find a sink point in a forest in the graph, assign the label
n to this sink point,then assign n-1 to next "sink point" and iterate in this fashion.


there may be forests in the directed acyclic graph


algo logic: each time we find a sink vertex we remove this vertex from the graph
and recursively do this until there is no vertex left in the graph

this algo is not good since we modify the graph every time we found a sink vertex
this is time consuming

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


graph = read_file('topologicalordertest.txt')

def removeSink(graph, sink):
    for vertex in graph.keys():
        if sink in graph[vertex]:
            graph[vertex].remove(sink)
            
    return graph



current_label = len(graph)
order = {}
graph_keys = list(graph.keys())

while len(order) < len(graph):
    for vertex in graph_keys:
    #in the 1st for loop all the sink vertices in the original graph will be found
        if len(graph[vertex]) == 0 and vertex not in order:
        #vertex is a sink vertex and haven't been put in the topological ordering
            order[vertex] = current_label
            current_label -= 1
            print(graph)
            graph = removeSink(graph, vertex)
            print(graph)





