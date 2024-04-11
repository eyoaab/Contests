t=int(input())
for _ in range(t):
    n,m,total=list(map(int,input().split()))
    n__=list(map(int,input().split()))
    m__=list(map(int,input().split()))
    counter=0
    n__.sort()
    m__.sort()

    for i in range(n):
        for j in range(m):
            if n__[i]+m__[j]<=total:
                counter+=1
    print(counter)            

