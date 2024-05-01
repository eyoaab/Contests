import sys


# class UnionFind:
#     def __init__(self, size):
#         self.parent = {i:i for i in range(size)}
#         self.size = {i:1 for i in range(size)}
    
#     def find(self, x):
#         while x != self.parent[x]:
#             self.parent[x] = self.parent[self.parent[x]]
#             x = self.parent[x]
#         return x
    
#     def union(self,x,y):
#         repx = self.find(x)
#         repy = self.find(y)

#         if repx != repy:
#             if self.size[repx] > self.size[repy]:
#                 self.parent[repy] = repx
#                 self.size[repx] += self.size[repy]
#             else:
#                 self.parent[repx] = repy
#                 self.size[repy] += self.size[repx]

print(2&3)