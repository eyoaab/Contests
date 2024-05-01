n,m,k = list(map(int,input().split()))
arr= []
for i in range(m+1):
    arr.append(int(input()))

ans = 0
for i in  range(m):
    num = arr[i]
    count = 0
    num ^= arr[-1]

    while num > 0:
        count += num & 1
        num >>= 1
        if count > k:
            break
    if count <= k:
        ans +=1 
print(ans)             