Problem:
given an undirected and unweighted (each edge weight 1) graph, find the smallest cut

Definition
what is a cut?
a cut (S,T) in an undirected graph G=(V,E) is a partition of vertices V into 2 non-empty, disjoint sets, S combine T = V.

Logic of the algorithm:
1. randomly choose an edge from the graph
***(here you need to think carefully how to implement the random picking that is truely pick an edge randomly!!!)***
2. then contract this edge
(contraction should follow the procedure in the textbook exactly, but i also have a different version)
3. repeat the process above until there are only 2 sets left and return the cut size

this randomized algorithm may return different answer for each run, so we need to run this algo for many times to make sure we can
get the right minimum cut answer.

when you implementing this algo with Python, the thing you should notice is that **DO NOT iterating an iterator while changing it!!!**
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

