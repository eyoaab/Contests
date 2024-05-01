
n = int(input())
v = []
for _ in range(n):
    v.append(tuple(map(int, input().split())))

temp = list(v)

l = r = 0
for i in range(n):
    l += v[i][0]
    r += v[i][1]

index = -1
mx_beauty = abs(l - r)

for i in range(n):
    tl, tr = l, r
    tl += (v[i][1] - v[i][0])
    tr += (v[i][0] - v[i][1])
    if abs(tl - tr) > mx_beauty:
        index = i + 1
        mx_beauty = abs(tl - tr)

if index == -1:
    print(0)
else
    print(index)


