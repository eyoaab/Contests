for _ in range(int(input())):
    s = input()
    b = s.count("B")
    o =len(s) - b
    if b == o:
        print("YES")
    else:
        print("NO")    
