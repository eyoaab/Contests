for _ in range(int(input())):
    n = int(input())
    bn = bin(n)
    
    if bn.count('1') == 1 and bn[2]=='1' and n!=1:
        print("NO")
    else:
        print("YES")    