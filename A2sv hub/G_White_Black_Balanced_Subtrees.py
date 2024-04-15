from collections import defaultdict
def to_parent(nums):
    parent = defaultdict(int)
    for i,j in enumerate(nums):
        parent[i] = j
    return parent    
def to_child(nums):
    child = defaultdict(list)
    for i,j in enumerate(nums):
        child[j].append(i)
    return child  

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    color = input()
    child = to_child(nums)
    parent = to_parent(nums)
    
