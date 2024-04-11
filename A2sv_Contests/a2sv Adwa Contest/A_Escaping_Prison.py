n = int(input())
for _ in range(n):
    k,h =  list(map(int,input().split()))
    max_=0
    for i in range(k):
        a,b=list(map(int,input().split()))
        max_ +=max(a,b)

    if max_ >=h:
        print("YES")
    else:
        print("NO")        