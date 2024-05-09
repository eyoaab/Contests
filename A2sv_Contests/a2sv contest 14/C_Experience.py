class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}
        self.value = {i:0 for i in range(size)}


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
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
n,m = map(int,input().split())
store = UnionFind(n+1)

for i in range(m):
    comand = input().split()
    
    if comand[0] == 'get':
        parent = store.find(int(comand[-1]))
        print(store.value[parent])
    elif comand[0] == 'join':
        store.union(int(comand[2]),int(comand[1]))  
    else:
        x,v = map(int,comand[1:])
        parent = store.find(x)
        store.value[x] += v


