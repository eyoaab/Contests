from collections import defaultdict
from bisect import bisect_left,bisect_right

nums = list(map(int,input().split()))
for _m in range(int(input())):
    pass

def to_adjecency_list(edges):
    graph = defaultdict(list)
    for edge in edges:
        node1,node2  = edge
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph


def isBipartite(self, graph):
    temp = defaultdict(bool)
    def dfs(node):
        if node not in temp:
            temp[node] = True
        for neg in graph[node]:
            if  neg not in temp:
                temp[neg] = not temp[node]
                dfs(neg) 
            if temp[neg] == temp[node]:
                return False
        return True 
    ans = True    
    for i in range(len(graph)):
        ans = ans and dfs(i)
    return ans    
                 """"
                 class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        prev = {}
        for i, edge in enumerate(edges):
            prev[i] = edge

        visited = set()
        max_length = 0

        for i in range(len(edges)):
            if i in visited:
                continue
            
            temp = []
            cur = i
            while cur not in visited:
                visited.add(cur)
                temp.append(cur)
                if cur==-1:
                    continue
                cur = prev[cur]
                
            if cur in temp: 
                cycle_length = len(temp) - temp.index(cur)
                max_length = max(max_length, cycle_length)

        return max_length if max_length >= 2 else -1
"""       

        



