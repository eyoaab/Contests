from collections import deque,defaultdict
from math import lcm
def calculate(orgional):
    c=0
    for i in range(len(orgional)):
        c += 1
        temp = orgional[i+1:] + orgional[:i+1]
        if temp == orgional:
            break       
    return c       
def to_graph(nums,name):
    graph = defaultdict(int)
    for i in range(len(nums)):
        graph[i+1] = nums[i]

    return graph    

def constract(lst,name):
    ans = []
    for i in lst:
        ans.append(name[i-1])
    return ans     

for _ in range(int(input())):
    n =int(input())
    word =input()
    nums = list(map(int,input().split()))
    graph = to_graph(nums,word)
    #print(graph)
    visited = set()
    answer = []
    c= []
    for i,j in graph.items():
        queue = deque([i])
        while queue:
            p = len(queue)
            for x in range(p):
                temp = queue.popleft()
                if temp in visited:
                    if c:
                        answer.append(c)
                        c= []
                    break
                else:
                    visited.add(temp)
                    queue.append(graph[temp])
                    c.append(temp)
    constracted  = [constract(arr,word) for arr in answer] 
    #print(constracted)
    val = [calculate(arr) for arr in constracted]               
    print(lcm(*val))

    
         

