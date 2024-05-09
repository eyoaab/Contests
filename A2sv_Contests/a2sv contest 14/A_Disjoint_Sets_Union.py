class UnionFind:

    def __init__(self, n):
        self.parent = {i:i for i in range(1,n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)
        if repy == repx:
            return

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]
n,m = map(int,input().split())
store = UnionFind(n+1)
for _ in range(m):
    flag,a,b = input().split()

    if flag == "union":
        store.union(int(a),int(b))
    else:
        a = int(a)
        b = int(b)
        if store.find(a) == store.find(b):
            print("YES")
        else:
            print("NO")        

