from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)
def to_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        node1,node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph
n,m = list(map(int,input().split()))
edges = []
for _ in range(m):
    edge = list(map(int,input().split()))
    edges.append(edge)
graph = to_graph(edges)


# go to code
answer = 0
visited = set()

def dfs(initial,arr):
    if initial in cant:
        return (arr,False)
    if initial in visited:
        return (arr,True)  
    visited.add(initial)
    arr.append(initial)

    for nod in graph[initial]:
        if nod in cant:
            return (arr,False)
        dfs(nod,arr)
        visited.add(nod)
    return (arr,True)

cant = set()
for i,j in graph.items():
    if len(j) != 2:
        cant.add(i)
for i,j in graph.items():
    if i in visited or i in cant:
        continue
    arry ,check = dfs(i,[])
    if check:
        answer += 1
        for k in arry:
            visited.add(k)

print(answer)            





