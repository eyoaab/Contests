class UnionFind:

    def __init__(self, n):
        self.parent = {i:i for i in range(1,n)}
        self.size = {i:1 for i in range(n)}
        self.mini_ = {i:i for i in range(n)}
        self.maxi_ = {i:i for i in range(n)}

    
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

                self.mini_[repx] = min(self.mini_[repx], self.mini_[repy])
                self.maxi_[repx] = max(self.maxi_[repx], self.maxi_[repy])
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]

                self.mini_[repy] = min(self.mini_[repy], self.mini_[repx])
                self.maxi_[repy] = max(self.maxi_[repy], self.maxi_[repx])

n,m = map(int,input().split()) 
store = UnionFind(n+1)

for _ in range(m):
    command = input().split()
    if command[0] == "union":
        a,b = command[1:]
        a = int(a)
        b = int(b)
        store.union(a,b)

    else:
        a = int(command[-1])
        parent = store.find(a)
        _mini = store.mini_[parent]
        _maxi = store.maxi_[parent]
        _size =  store.size[parent]

        print(_mini,_maxi,_size)    



