import math
t=int(input())
for _ in range(t):
    ans=0
    a,b,c=list(map(int,input().split()))
    ans+=a

    l=3-(b%3)
    
    if c<l and b%3!=0:
        print(-1)
    else:
        b+=l
        c-=l
        ans+=b//3
        print(ans+(math.ceil(c/3)))    