#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:52:05 2018

@author: BNZ
"""


'''
DFS explores the graph aggressively, to go forward into branch while there is such
possibility, only backtracks to shallow nodes when it reaches an end.
after running DFS, if v marked as explored <==> there exists a path from s to v, not vice versa!!!
NOTE:
    here is the difference with BFS, in the directed graph reachable is not for each other anymore.
    in a directed graph, there can be forests, DFS can only give you the reachable vertices of initial_node.


running time is the same as BFS, which is O(n_s + m_s)


every directed acyclic graph must has a sink vertex
we can compute the topological ordering from finding the sink vertex in the graph
the last vertex in the topological ordering is the sink vertex


in the directed graph, DFS can be used to solve SCCs problem
< i think in the Kosaraju algorithm, using 2 DFS to find SCCs because in a directed
graph, reachable from each other is not guaranteed from just 1 DFS>


1. recusive version
2. iterative version

'''


# recuresive version

def dfsRecursive(graph, initial_node):
    """
    the directed graph is represented as dict[node] = [neighbors]
    explore the graph from the initial_node recursively
    returns a list of vertices that only reachable from initial_node
    
    NOTE: vertices in the returned list are not guaranteed to be reachable from each other 
    """
    global explored
    # each time we recursively call dfsRecursive will alter explored
    # so we need to make explored a global variable

    if len(graph[initial_node]) > 0:
    # adding this if condition cuz there can be situation where there is no
    # vertices can be reachable from the initial_node
        for neighbor in graph[initial_node]:
            if neighbor not in explored:
                explored.append(neighbor)
                dfsRecursive(graph, neighbor)
    else:
        print('The initial_node has no outgoing edges, please change the initial_node.')

    return explored



# iterative version using a FILO stack

import copy

def dfsStack(graph, initial_node):
    """
    using a FILO stack to iteratively explore the graph
    """
    explored = []
    stack = [initial_node]
    
    graph_copy = copy.deepcopy(graph)
    # use a copy to avoid modify the original graph
    
    while stack:
        neighbors_copy = graph_copy[stack[-1]]
        # FILO ==> the check always starts from the last element in the stack
        
        for i in neighbors_copy:
            if i not in explored:
                explored.append(i)
                stack.append(i)
                break
        # since we are agressively exploring the graph, after we append i into stack
        # we need to jump out the for loop and going forward exploring the node
        # we just append to the stack, which is stack[-1]
            else:
                neighbors_copy.remove(i)
                continue
            # remove i from neighbors of stack[-1] if i has been explored
            # then continue this for loop to check if there exist the possibility
            # to go further.
            # if all the neighbors of stack[-1] have been explored then
            # neighbors_copy should be empty and we should backtrack the graph
            # by removeing stack[-1] and explore the new stack[-1] in the same fashion
            
        if not neighbors_copy:
            stack.pop(-1)
        # FILO ==> remove the stack[-1] if all its neighbors have been explored
            
    return explored




def read_file(file_name):
    """
    represent the directed graph as dict[vertex] = [neighbors]
    key is the vertex
    value is a set contains the connected vertices of that key/vertex
    """
    graph = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip().split(' ')
            if int(line[0]) not in graph:
                graph[int(line[0])] = [int(line[1])]
            else:
                if line[0] != line[1]:
                    graph[int(line[0])].append(int(line[1]))
            
    return graph


import random

graph = read_file('test3.txt')
initial_node = random.randint(1, len(graph.keys()) - 1)
print('initial_node is ', initial_node)

# recursive version
explored = []
dfsRecursive(graph, initial_node)

# stack version
explored1 = dfsStack(graph, initial_node)


print(set(ele for ele in explored) == set(ele for ele in explored1))
# here use set cuz the order of the elements in these 2 lists may not the same
# with different order, the result will be negative eventhough the elements are the same 


