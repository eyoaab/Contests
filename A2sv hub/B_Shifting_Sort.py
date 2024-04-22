for _t in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = []
    for i in range(n):
        for j in range(i+1):
            if a[j] >= a[i]: break
        if j < i:
            a[j:i+1] = [a[i]] + a[j:i]
            b.append((j+1, i+1, i-j))

    print(len(b))
    for (l,r,d) in b:
        print(l, r, d)