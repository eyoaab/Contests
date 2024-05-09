n,m,k = list(map(int,input().split()))
arr= [int(input()) for i in range(m+1)]
ans = 0

for num in arr[:-1]:
    # num = arr[i]
    count = 0
    num ^= arr[-1]

    
    if bit_count() <= k:
        ans +=1 
print(ans)             