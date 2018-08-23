#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:54:25 2018

@author: BNZ
"""

'''
problem: 
given an undirected and unweighted graoh, find the smallest  cut

a cut (S, T) in an undirected graph G = (V, E) is a partition of vertices V into 2 non-
empty, disjoint sets, S combine T = V.


randomly choose an edge from the graph ==> contract this edge

contraction should follow the certain procedure exactly, but here I use a bit different
way


repeat the process above until there are only 2 sets left and return the cut size


this randomized algorithm may return different answer for each run, and we run this algo
for many times then take the minimum count as the minimum cut of the input graph
(of course, the answer may be wrong, depending on how many times you run it/the input etc.)

'''

# how about the vertices?
# in this way, I initiate the vertices list as each vertix in the graph being an 
# individual set, merge the 2 vertices sets of the end points of the random picked
# edge.
# how about the edges?
# in this way, since the edges are undirected, each edge in the graph will be
# represented by a set with 2 endpoints in it. during the edge contraction, I
# only remove the loops in the graph and allow the prosibility of multigraph by
# checking if an edge's endpoints are in the same vertices set.


'''
after writing this piece, the thing I learned is
"DO NOT ITERATING A LIST WHILE CHANGING IT!!!"
there can be problem causing by certain special cases.

for example, let l = [1,2,2,3,4,5], say you want to remove all the 2s in l.
but what will happen if you run
for i in l:
    if i == 2:
        l.remove(i)

the result is l becomes [1, 2, 3, 4, 5], there is still a 2 in l since in this
special case 2s are neighbors. since you remove the 1st 2 which changed l,
all the elements in l after the 1st 2 will be moved forward and the index of
the 2nd 2 becomes the index of the 1st 2 and will be missed as i points to index
2 which is pointing 3 during the iteration.

'''



def read_file():
    V = []
    E = []
    file = open('kargerMinCut.txt')
    for line in file:
        line = line.strip().split('\t')
        V.append({int(line[0])})
        for i in line[1:]:
            if {int(line[0]), int(i)} not in E:
                E.append({int(line[0]), int(i)})
        # E.append([int(l[0]), int(x)] for x in l[1:])
        # [<generator object read_file.<locals>.<genexpr> at 0x10ffa0678>, <generator object read_file.<locals>.<genexpr> at 0x10ffa0570>
        # ???
    return V, E



import random


def contraction(random_edge, V, E):
    
    v1, v2 = random_edge
    
    # contraction in my way
    for i in V:
        if v1 in i:
            set1 = i
            

    for i in V:
        if v2 in i:
            set2 = i
    
    union_set = set1.union(set2)
    V.remove(set1)
    V.remove(set2)
    V.append(union_set)

    '''
    for i in E:
        print(i)
        if len(i.intersection(union_set)) == 2:
            print(i)
            E.remove(i)
    
    iterate the list while changing sometimes will causing problems if the elements
    in the list satisfy some special case!!!
    
    note: can not use E1=E to solve this problem since for mutable list they
    are the same object
    '''
    
    E1 = E.copy()
    # the solution of the problem above
    # iterate one list while changing another one
    for i in E1:
        if len(i.intersection(union_set)) == 2:
            E.remove(i)

    return V, E
                                                                    
    

def kargerMinCut(V, E):
    """
    while there are more than 2 sets in the vertices list continue pick an
    random edge from the updating graph and doing the edge contraction
    
    """
    
    while len(V) > 2:
        
        random.shuffle(E)
        random_edge = random.choice(E)
        # an random picked edge represented by a set with 2 vertices
        # this implement is truely randomly pick an edge uniformly
        
        E.remove(random_edge)
        # remove the edge we picked immediately
        
        V, E = contraction(random_edge, V, E)
        # doing the edge contraction
        # return the modified gragh
        
        kargerMinCut(V, E)
        # work on the modified gragh until there are only 2 sets of
        # non-empty, disjoint vertices set left
        
    return len(E)
    


V, E  = read_file()
# print(V[:13])
# [{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}]
# print(len(V))
# 200
# print(E[:13])
# [{1, 37}, {1, 79}, {1, 164}, {1, 155}, {32, 1}, {1, 87}, {1, 39}, {1, 113}, {1, 15}, {1, 18}, {1, 78}, {1, 175}, {1, 140}]
# print(len(E))
# 2517



'''
for i in range(11):
    min_cut = 500
    for i in range(51):
        V, E  = read_file()
        cut = kargerMinCut(V, E)
        if cut < min_cut:
            min_cut = cut
            
    print(min_cut)

# there are 8 times 17, 2 times 20
'''


min_cut = 500
for i in range(101):
    V1  = V.copy()
    E1 = E.copy()
    cut = kargerMinCut(V1, E1)
    if cut < min_cut:
        min_cut = cut
        
print(min_cut)

# the kargerMinCut() we modify the graph in place in this way
# so each time before we call kargerMinCut() we copy the graph as V1, E1




















