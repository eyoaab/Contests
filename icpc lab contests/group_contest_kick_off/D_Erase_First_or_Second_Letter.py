from collections import defaultdict
for _ in range(int(input())):
    n =int(input())
    nams =input()
    c = {}
    for i in nams:
        c[i]=n
    ans = 0
    for i in range(n-1,-1,-1):
        val = c[nams[i]]
        ans += val-i
        c[nams[i]] = i
    print(ans)    

