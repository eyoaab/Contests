class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        uf.union(int(query[1]) - 1, int(query[2]) - 1)
    elif query[0] == '2':
        for i in range(int(query[1]) - 1, int(query[2])):
            uf.union(i, i + 1)
    else:
        if uf.find(int(query[1]) - 1) == uf.find(int(query[2]) - 1):
            print("YES")
        else:
            print("NO")
