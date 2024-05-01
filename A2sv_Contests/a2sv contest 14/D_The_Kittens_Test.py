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
                answer[repx].extend(answer[repy])
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]
                answer[repy].extend(answer[repx])


n = int(input())

answer = [[i] for i in range(n + 1)]

union_find = UnionFind(n)

for _ in range(n - 1):
    a, b = [int(i) for i in input().split()]

    union_find.union(a, b)

for ans in answer:
    if len(ans) == n:
        print(*ans)
        break

