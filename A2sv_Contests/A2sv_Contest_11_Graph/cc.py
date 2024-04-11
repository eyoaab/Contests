from collections import defaultdict, deque
def to_graph(edges):
    graph = defaultdict(list) 
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1) 
    return graph

n = int(input())
edges = []
for _ in range(n - 1):
    edge = list(map(int, input().split()))
    edges.append(edge)

graph = to_graph(edges)
left = []
right = []
queue = deque([(1, 0)]) 
visited = set()  
while queue:
    v, level = queue.popleft()
    if v in visited:
        continue
    visited.add(v)
    if level % 2 == 0:
        left.append(v)
    else:
        right.append(v)
    for neig in graph[v]:
        queue.append((neig, level + 1))

ed = (len(left) * len(right)) - (n - 1)
print(ed)
