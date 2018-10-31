
**Course2 Graph Search, Shortest Paths, and Data Structures**
1. Week1 - Graph Search and Connectivity
2. Week2 - Topological Sort/Kosaraju Algorithm for Computing SCCs
3. Week3 - Heap/Dijkstra's Single Source Shortest Path Algorithm
4. Week4 - Data Structures(Binary Search Trees/Hash Table/Bloom Filter)/2-SUM Problem





Basics you need know


**Graph**

a graph is a representation of the pairwise relationships between objects

vertices/nodes -> the objects being represented in the graph
V -> vertex set of the whole graph

edges -> pairwise relationships in the graph
E-> edge set of the whole graph

the graph, then, can be denoted as G = (V, E)

---
**Undirected Graph**

`unordered` pair {u, v} of vertices is an edge in the graph
u and v are called endpoints of the edge
2 edges (u, v) and (v, u) are the same
if there exist an edge (u, v) or (v, u) then u and v are ***reachable from each other***

---
**Directed Graph**

an `ordered` pair of vertices, is denoted as (u, v), means that the edge is traveling from u to v
if there exist an edge (u, v) in the graph then v is reachable from u, but u is not rachable from v if there is no edge (v, u)
tail of the edge -> u, is said to be a directed predecessor of v
head of the edge -> v, is said to be a directed successor of u

---
**Measuring the Size of a Graph**

usually, the running time of a algorithm is a function of the input size
for a algo like sorting, the input size is easy to define, which is the length of the input array
however, for a graph, we must specify some thing to make sure what we mean by "size"
- a directed graph or a directed graph
- how the graph is represented

two parameters control a graph's size:
1. the # of vertices in the whole graph -> n = |V|
2. the # of edges in the whole graph ->  m = |E|


now let's think about this question first:
`in a connected undirected graph with no "parallel edges", how the # of edges depend on the # of vertices?`
- parallel edges -> at most 1 undirected edge can be existed between each pair of vertices
- connected graph -> the graph is "in 1 piece"
>at least m is n-1, that is the # of edges m is linear in the # of vertices, $m = \Omega(n)$
>at most m is n(n-1)/2 when each pair vertices in the graph has an edge, which is called ***complete graph***, that is $m = O(n^2)$

**Conclusion**
in a connected undirected graph with no parallel edges, the # of edges is between $m = \Omega(n)$ and $m = O(n^2)$

***sparse and dense***
sparse -> the # of edges in the graph is close to $m = \Omega(n)$
dense -> the # of edges in the graph is close to $m = O(n^2)$

---
**Representing a Graph**
- adjacency list
	- an array containing the graph's vertices
	- an array containing the graph's edges
	- for each edge, a pointer to each of its 2 endpoints
	- for each vertex, a pointer to each of the incident edges (incoming)
>these 2 arrays (linked lists) cross-reference each other in the natural way, with each edge associated with pointers to its endpoints and each vertex with pointers to the edges for which it is an endpoint.

what's more for a directed graph?
each edge keeps track of which endpoint is the tail and which endpoint is the head
each vertex maintains 2 arrays of pointers, 1 for the outgoing edges and 1 for the incoming edges

- adjacency matrix



**DAG**

Definition:
A DAG is a directed acyclic graph, at least has 1 source vertex and 1 sink vertex.
- source vertex -> a vertex only has outgoing edges, with no incoming edges.
- sink vertex -> a vertex only has incoming edges, with no outgoing edges.




