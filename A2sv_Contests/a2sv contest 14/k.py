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
n = int(input()) 
nums = list(map(int,input().split()))
model = UnionFind(n+1)
for i in range(1,n+1):
    model.union(nums[i-1],i)
    
answer = 0
for i in range(1,n+1):
    if model.parent[i] == i:
        answer += 1
  
print(answer)                      