t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    halph=n-k
    if k==halph*2:
        print("YES")
    else:
        print("NO")    