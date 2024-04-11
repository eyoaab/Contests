for _ in range(int(input())):
    a,b,k =list(map(int,input().split()))
    if a==b:
        if a==1:
            print("NO")
        else:
            print("YES")
    else:
        n = b - a + 1
        odd = n//2
        if a%2 != 0 and b%2 != 0:      
            odd += 1 
            
        if odd > k:
            print("NO")
        else:
            print("YES")
       
