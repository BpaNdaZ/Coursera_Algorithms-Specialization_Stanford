# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:07:23 2018

@author: BNZ
"""


def read_input(file_name):

    """
    represent the input as dict[key] = value
    keys are the vertices(tails) in the input graph
    values are lists that contain 2 elements: 1st is the head, 2nd is the weight of the edge
    """
    graph = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip().split('\t')
            graph[int(line[0])] = []
            for group in line[1:]:
                graph[int(line[0])].append([int(ele) for ele in group.split(',')])

    return graph

# in this input file, there is no


'''
The Single-Source Shortest Path Problem


Dijkstra Algorithm:

- works on any directed graph with nonnegative edge lengths
- computes the lengths of shortest paths from a starting vertex to all other vertices

1. starting from the start_vertex, which has the shortest path 0
2. keep a explored set in which every vertex in it has already found its shortest path from start vertex
3. search every edges connect the explored set & complement set to find the vertex in the complement set \
with the smallest shortest path, add this vertex to explored set
    3_1. means every iteration of Dijkstra algorithm processes one new vertex, the head of an edge crossing \
    from the explored set to complement set
4. do 3. repeatedly until all the vertices are in the explored set




Why Not BFS?
- using BFS to solve this problem is a special case of Dijkstra algorithm, where all the weights of \
edges are 1
- BFS computes the minimum # of edges in a path from the starting vertex to every other vertex, however, \
with general nonnegative edge lengths, a shortest path need not be a path with the fewest # of edges
- in theory, this problem can be also solved using BFS by expanding edges into paths of length-1 edges \
and applying BFS, but the problem of this reduction is that it blows up the size of the graph if the \
weights are large
- further more, even if the BFS can be applied, the running time is not linear on the original graph



What About Nonnegative edges?
1. Can't we just force all the edge lengths to be nonnegative by adding a big enough number to every edge?
the problem of this solution comes from different paths from 1 vertex to another might not have the same \
# of edges, then the lengths of different paths can increase by different amounts
means that the shortes path in the new graph might be different than in the original graph

2. even with extremely simple graph with negative edge lengths, Dijkstra algorithm will give the wrong answer
if the selected minimum Dijkstra score of an edge from explored set to complement set is negative, this \
doesnot mean this is the shortest path from starting vertex to that head
for example, u->1->v->-3>w; u->-1->w, certainly Dijkstra algorithm will pick s->-2->t as the shortest path \
which is wrong

'''


class Dijkstra(object):

    def __init__(self, graph):

        self.graph = graph
        self.explored_set = set()  # contains vertices already have the shortest path for sure
        self.shortest_path = {}  # record the result

        for vertex in graph.keys():
            self.shortest_path[vertex] = 100000000

    def find_shortest_path(self, starting_vertex):
        self.explored_set.add(starting_vertex)
        self.shortest_path[starting_vertex] = 0
        self.explored_set.add(starting_vertex)

        while self.explored_set != set(self.graph.keys()):
            # go through every vertex in the explored_set
            # assign a computed shortest path to vertices can be reached from the explored_set
            # find the minimum one, which is the result of each for loop and add to the explored_set
            weight_arch = 100000000
            min_vertex = 0
            for vertex in self.explored_set:  # vertex is in explored_set for sure
                complement_set = set(graph.keys()).difference(self.explored_set)
                for head in graph[vertex]:
                    if head[0] in complement_set:  # only for the edges that connects explored_set \
                        # and complement_set
                        if self.shortest_path[vertex] + head[1] < weight_arch:
                            weight_arch = self.shortest_path[vertex] + head[1]
                            min_vertex = head[0]

            self.explored_set.add(min_vertex)
            self.shortest_path[min_vertex] = weight_arch

        return self.shortest_path

import time

start = time.time()
graph = read_input('DijkstraData.txt')
reading = time.time()
print('reading file is finished', reading-start)

dijkstra = Dijkstra(graph)
starting_vertex = 1
dijkstra_shortest_path_dict = dijkstra.find_shortest_path(starting_vertex)
print(dijkstra_shortest_path_dict[7],dijkstra_shortest_path_dict[37],dijkstra_shortest_path_dict[59],
      dijkstra_shortest_path_dict[82],dijkstra_shortest_path_dict[99],dijkstra_shortest_path_dict[115],
      dijkstra_shortest_path_dict[133],dijkstra_shortest_path_dict[165],dijkstra_shortest_path_dict[188],
      dijkstra_shortest_path_dict[197])
finishing = time.time()
print('Dijkstra is finished', finishing - reading)
# 2599 2610 2947 2052 2367 2399 2029 2442 2505 3068





'''
for starting_vertex in range(1, 201):
    dijkstra = Dijkstra(graph)
    dijkstra_shortest_path_dict = dijkstra.find_shortest_path(starting_vertex)

    for i in dijkstra_shortest_path_dict:
        if dijkstra_shortest_path_dict[i] == 100000000:
            print('%r is not reachable from %r' % (i, starting_vertex))

# vertices in the graph are reachable from each other
'''























