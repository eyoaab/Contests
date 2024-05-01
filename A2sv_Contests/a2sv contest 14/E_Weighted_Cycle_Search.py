from collections import defaultdict, deque

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(1, size + 1)}
        self.size = {i:1 for i in range(1, size + 1)}
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]

def dfs(node, path):
    if node == b:
        return path
        





for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    graph = defaultdict(list)
    union_find = UnionFind(n)
    min_ans = []

    edges = []

    for i in range(m):
        edges.append([int(i) for i in input().split()])

    edges.sort(key = lambda x: x[2], reverse=True)

    for a, b, w in edges:
        if union_find.find(a) == union_find.find(b):
            min_ans = [a, b, w]
        
        else:
            graph[a].append(b)
            graph[b].append(a)
        
        union_find.union(a, b)
    
    path = bfs(min_ans[0], min_ans[1])

    print(min_ans[2], len(path))

    print(*path)

    





