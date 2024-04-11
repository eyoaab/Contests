from collections import defaultdict

def to_adjecency_list(edges):
    graph = defaultdict(list)
    for edge in edges:
        node1,node2  = edge
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

n,m = list(map(int,input().split()))
edges = []
for i in range(m):
    edge = list(map(int,input().split())) 
    edges.append(edge)
    
graph = to_adjecency_list(edges)
values = graph.values()
temp = [len(x) for x in values]
if temp.count(1)==2 and temp.count(2)==n-2:
    print("bus topology")
elif temp.count(2) == n:
    print("ring topology")
elif temp.count(1) == n-1:
    print("star topology")         
else:
    print("unknown topology")