for _ in range(int(input())):
    n,a,b = list(map(int,input().split()))
    if b/2 >a:
        print(n*a)
    else:
        if n%2==0:
            print((n//2)*b)
        else:
            ans= (n//2)*b 
            print(ans+a)      