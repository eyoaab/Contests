from collections import defaultdict
v = defaultdict(list)
mx = -1

def dfs(x, level):
    global mx
    stack = [(x, level)]
    while stack:
        node, lvl = stack.pop()
        mx = max(mx, lvl)
        for i in v[node]:
            stack.append((i, lvl + 1))

n = int(input())
a = [0] * (n + 1)
x_values = [int(input()) for i in range(n)]

for i in range(1, n + 1):
    x = x_values[i - 1]
    a[i] = x
    if x != -1:
        v[x].append(i)
    else:
        v[0].append(i)

for i in range(len(v[0])):
    dfs(v[0][i], 1)

print(mx)
