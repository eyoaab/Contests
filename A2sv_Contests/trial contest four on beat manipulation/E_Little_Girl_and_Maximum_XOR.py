l, r = map(int, input().split())
res = 0
b = 1
while l != r:
    res += b
    l >>= 1
    r >>= 1
    b <<= 1
print(res)

    
