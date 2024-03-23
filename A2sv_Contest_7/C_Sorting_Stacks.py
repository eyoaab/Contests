t=int(input())
for _ in range(t):
    n=int(input())
    extra=0
    input_li=list(map(int,input().split()))
    flag=True
    for i in range(n):
        if extra+input_li[i]<i:
            flag=False
            break  
        else:
            extra+=input_li[i]-i 

    if flag:
        print("YES")
    else:
        print("NO")              

