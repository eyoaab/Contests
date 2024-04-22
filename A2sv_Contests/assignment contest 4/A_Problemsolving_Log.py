from collections import *
for _ in range(int(input())):
    n = int(input())
    s = input()
    count = Counter(s)
    referance = {k:ord(k)-64 for k in set(s)}

    ans = 0
    for i,j in count.items():
        if j >= referance[i]:
            ans +=1
    print(ans)        
            
    