from collections import*
from heapq import *
nums = list(map(int,input().split()))
def to_graph(edges):
    graph = defaultdict(list)

    for node1,node2 in edges:
        graph[node2].append(node1)
        graph[node1].append(node2)

    return graph    
