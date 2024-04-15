for _ in range(int(input())):
    n,a,b =  list(map(int,input().split()))
    if b/2 >=a:
        print(a*n)
    else:
        temp  = (n//2)*b
        temp += (n%2)*a
        print(temp)

