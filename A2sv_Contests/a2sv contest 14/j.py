for _ in range(int(input())):
    s = input()
    if len(s)%2!=0:
        print("NO")
    else:
        n =len(s)//2
        if s[:n] == s[n:]:
            print("YES")
        else:
            print("NO")        