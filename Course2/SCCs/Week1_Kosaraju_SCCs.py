# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:20:06 2018

@author: BNZ
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
        #{vertex:its SCC's leader}



def dfs(graph, initial_vertex, tracker):
    """
    recursively dfs search from the initial_vertex
    assign the topo order to vertices that is reachable from the initial_vertex
    along this single aggressively dfs 
    """
    tracker.explored.add(initial_vertex)
    tracker.SCC[initial_vertex] = tracker.leader
    for head in graph[initial_vertex]:
        if head not in tracker.explored:
            dfs(graph, head, tracker)
    
    # assign a finishing time to each vertex gives the topo order
    tracker.finish_time[initial_vertex] = tracker.current_time       
    tracker.current_time -= 1
    

def dfs_graph(graph, vertices_graph, tracker):
    """
    apply the dfs to the whole graph to get the topo ordering of the graph
    """
    for vertex in vertices_graph:
        if vertex not in tracker.explored:
            tracker.leader = vertex
            dfs(graph, vertex, tracker)


from itertools import groupby
from collections import OrderedDict

def findSCCs(graph):
    """
    using Kosaraju algo to find SCCs in the graph
    return the SCCs as {leader:[vertices in the same SCC including the leader]}
    """
    # 1st run the dfs on reversed graph to find a topo order, which contains \
    # in the Tracker.finish_time
    reversed_graph = reverse_graph(graph)
    dfs1_tracker = Tracker(reversed_graph)
    vertices_graph = list(reversed_graph.keys())
    dfs_graph(reversed_graph, vertices_graph, dfs1_tracker)
    # lining the vertices in the asceding topo order of the reversed graph
    # source SCCs in the reversed graph is the sink SCCs in the original graph
    # start search the original graph from a vertex in the source SCCs in the \
    # reversed graph equals start search from a vertex in the sink SCCs
    asceding_topo = sorted(dfs1_tracker.finish_time,
                           key=lambda x:dfs1_tracker.finish_time[x])
    # return the list of vertices in the ascending finish time
    # {vertex:finish_time}
    # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    
    # 2nd Tracker is used for keeping the parameters we later for grouping \
    # vertices in the same SCC
    dfs2_tracker = Tracker(graph)
    dfs_graph(graph, asceding_topo, dfs2_tracker)
    
    # Tracker.SCC is represented as {vertex:its SCC's leader}
    # so we need to group the vertices in the same SCC by the parameter leader
    # the iterable input groupby function need to be sorted on the same key \
    # function
    SCC_dict = {}
    ordered_SCC = OrderedDict(sorted(dfs2_tracker.SCC.items(),
                                     key=lambda x:x[1]))
    for leader, v_SCC in groupby(ordered_SCC, key=ordered_SCC.get):
        SCC_dict[leader] = list(v_SCC)
    
    '''
    SCC_dict = {}
    for lead, SCC in groupby(sorted(dfs2_tracker.SCC, key=dfs2_tracker.SCC.get),
                             key=dfs2_tracker.SCC.get):
        SCC_dict[lead] = list(SCC)
    '''
    
    
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
    
    
    # convert the SCCs into how many vertices in each SCC
    # and then return the 5 biggest SCCs' # of vertices in them
    result = list(map(len, SCC.values()))
    result.sort(reverse=True)
    
    '''
    # another way to find the biggest 5 SCCs using heapq 
    top_5 = heapq.nlargest(5, SCC, key=lambda x: len(SCC[x]))
    # find the biggest 5 SCCs in the graph
    result = []
    # append the biggest 5 in the result
    for i in range(5):
        try:
            result.append(len(SCC[top_5[i]]))
        except:
            result.append(0)
    '''
    
    print(result[:5])



if __name__ == '__main__':
    
    threading.stack_size(67108864)
    sys.setrecursionlimit(10 ** 6)
    thread = threading.Thread(target=main)
    thread.start()



# https://github.com/javon27/SCC/blob/master/scc.py


# how to use groupby
# how to sort a dict
# how to use map
# not fully understand how the threading works







