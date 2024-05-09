

for i in range(int(input())):
    n,m,r,c = list(map(int,input().split()))
    x,y =0,0 
    if abs(n-r) > r - 1:
        x = n
    else:
        x = 1
    if abs(m -c) > c - 1:
        y = m
    else:
        y = 1
    p1,p2 = 1,1
    if x < n:    
        p1 = n
       
    if y < m:
        p2 = m

    print(x,y,p1,p2)    
