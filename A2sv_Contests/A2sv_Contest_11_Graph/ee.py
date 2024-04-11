from collections import defaultdict
def to_adjecency_list(edges):
    graph = defaultdict(list)
    for edge in edges:
        node1,node2  = edge
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph
n = int(input())
edges = []
for i in range(n-1):
    edge = list(map(int,input().split())) 
    edges.append(edge) 
graph = to_adjecency_list(edges)
orgional = list(map(int,input().split())) 
expected = list(map(int,input().split())) 
ans  =[i+1 for i in range(n) if orgional[i] != expected[i]]
print(len(ans))
for i in ans:
    print(i)
