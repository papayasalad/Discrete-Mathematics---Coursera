# The algorithm should check all the permutations of the vertices and return the
# minimum weight of a cycle visiting each vertex exactly once.
import networkx as nx
from itertools import permutations
import sys

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    min_weight = sys.maxsize
    
    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        # Write your code here.
      sum_weight = 0
      i = 0
      while i < n - 1:
        sum_weight += g[p[i]][p[i+1]]['weight']
        i += 1
      sum_weight += g[p[i]][p[0]]['weight']
      if sum_weight < min_weight:
        min_weight = sum_weight
    return min_weight
