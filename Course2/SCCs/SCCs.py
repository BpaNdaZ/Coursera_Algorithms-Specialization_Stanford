# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:20:06 2018

@author: hp
"""


'''
Definition of SCCs:
the strongly connected components (SCCs) of a directed graph G are the
equivalence classes of the relation, that is the maximal regions within which
you can get from anywhere to anywhere else

#equivalence relation ==> cycles
u<->v means that u and v are reachable from each other in the directed graph
this means that there can be cycles in the given directed graph

here we use Kosaraju Algorithm to solve the SCCs problem, procesure of  this algo
1. using DFS on the original graph to find the topological ordering
2. using the reversed topological order that we found to do another DFS on the
reversed graph to find SCCs


the key idea behind this algorithm is topological sort
- in a DAG, the last vertex in the topological ordering must be 1 of the sink vertices
of the DAG
- however, in a directed graph with cycle, the last vertex in the topological ordering
doesn't have to be in the sink SCC, depends on where you start the DFS; But the first
vertex in the topological ordering will be in the source SCC (the SCC only has outgoing
edges, no incoming edges)

with this property you can easily see that if we reverse the original graph, the
source SCC will become a sink SCC (no outgoing edges, only incoming edges), and
if we DFS the reversed graoh from the 1st vertex in the reversed topological order
we will start the search from a sink SCC, which can lead to the right answer

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
    automatically remove the self loop vertex when build up the graph
    key is the tail of an edge
    value is a list contains all the heads of that key/vertex
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


from collections import defaultdict

def reverse_graph(graph):
    """
    given a directed graph which is represented as dict[tail] = [head_list], compute
    a reversed graph, in which every edge in the original graph changes direction
    careful about the source vertices in the original graph, if building the
    reversed graph in an inappropriate way source vertices will disappear
    """
    reversed_graph = defaultdict(list) 
    for tail, head_list in graph.items():
        if tail not in reversed_graph:
            reversed_graph[tail]
        for head in head_list:
            reversed_graph[head].append(tail)
    
    return reversed_graph



class Tracker(object):
    """
    this Tracker is used for keep track all the important parameters during
    the dfs
    """
    def __init__(self, graph):
        self.current_time = len(graph)
        #the largest current_time will be assign to 1 of the sink vertices in
        #the graph
        self.finish_time = {}
        #keep track the finish_time of each vertex
        #respent as {vertex:finish_time}
        self.explored = set()
        #contains all the visited vertices during the dfs
        self.leader = None
        #assign a leader for each SCC, which can be used later for finding
        #all vertices with the same leader that means in the same SCC
        self.SCC = {}
        #find SCCs in the graph, represent as
        #{leader:[all vertices in the the same SCC including leader]}



def dfs(graph, initial_vertex, tracker):
    """
    recursively dfs search from the initial_vertex
    """
    tracker.explored.add(initial_vertex)
    tracker.SCC[initial_vertex] = tracker.leader
    for head in graph[initial_vertex]:
        if head not in tracker.explored:
            dfs(graph, head, tracker)
    
    tracker.finish_time[initial_vertex] = tracker.current_time       
    tracker.current_time -= 1
    

def dfs_graph(graph, vertices_graph, tracker):

    for vertex in vertices_graph:
        if vertex not in tracker.explored:
            tracker.leader = vertex
            dfs(graph, vertex, tracker)


from itertools import groupby

def findSCCs(graph):
    
    reversed_graph = reverse_graph(graph)
    dfs1_tracker = Tracker(reversed_graph)
    vertices_graph = list(reversed_graph.keys())
    
    dfs_graph(reversed_graph, vertices_graph, dfs1_tracker)
    
    reversed_topo = sorted(dfs1_tracker.finish_time,
                           key=dfs1_tracker.finish_time.get)
    #D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    
    dfs2_tracker = Tracker(graph)
    dfs_graph(graph, reversed_topo, dfs2_tracker)
    
    SCC_dict = {}
    for lead, SCC in groupby(sorted(dfs2_tracker.SCC, key=dfs2_tracker.SCC.get),
                             key=dfs2_tracker.SCC.get):
        SCC_dict[lead] = list(SCC)
        
    return SCC_dict

import heapq
import time
import sys
import threading


def main():
    start = time.time()
    graph = read_file('SCC.txt')
    t1 = time.time() - start
    print(t1)
    SCC = findSCCs(graph)
    t2 = time.time() - start
    print(t2)
    top_5 = heapq.nlargest(5, SCC, key=lambda x: len(SCC[x]))
    #sorted_groups = sorted(groups, key=lambda x: len(groups[x]), reverse=True)
    result = []
    for i in range(5):
        try:
            result.append(len(SCC[top_5[i]]))
            #result.append(len(groups[sorted_groups[i]]))
        except:
            result.append(0)
    print(result)



if __name__ == '__main__':
    
    threading.stack_size(67108864)
    sys.setrecursionlimit(10 ** 6)
    thread = threading.Thread(target=main)
    thread.start()



# https://github.com/javon27/SCC/blob/master/scc.py










