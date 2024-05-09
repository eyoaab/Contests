
for _ in range( int(input())):
    n, z = map(int, input().split())
    a = list(map(int, input().split()))
    max_ = 0
        
    for i in range(n):
        a[i] = a[i] | z
        z = a[i] & z
        max_ = max(max_, a[i])
    
    print(max_)
