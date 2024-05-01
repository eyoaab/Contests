from sys import stdin
input = stdin.readline
n, m = map(int, input().split())


parent = {i:i for i in range(n)} 
size = {i:1 for i in range(n)}
    
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union( x, y):
    rooty = find(y)
    rootx = find(x)
    if size[rootx] > size[rooty]:
        parent[rooty] = rootx
        size[rootx] += size[rooty]
    else:
        parent[rootx] = rooty
        size[rooty] += size[rootx]
            
def connected( x, y):
    return find(x) == find(y)
    
for _ in range(m):
    groupi = list(map(int, input().split()))
    sz, group = groupi[0], groupi[1:]
    for i in range(1, sz):
        union(group[0]-1, group[i]-1)

res = []
for i in range(n):
    res.append(size[find(i)])

print(*res)
