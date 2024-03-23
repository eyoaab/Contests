from bisect import bisect_left,bisect_right
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
query=list(map(int,input().split()))
prefix=[0]
for i in range(n):
    prefix.append(prefix[-1]+nums[i])
for q in query:
    x=bisect_left(prefix,q)
    print(x)
    
