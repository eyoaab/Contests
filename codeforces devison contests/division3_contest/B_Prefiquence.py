for T in range(int(input())):
    n,m = list(map(int,input().split()))
    first =input()
    second =input()
    s=0
    count = 0

    for f in range(n):
        while s < m and second[s] != first[f]:
            s+=1
        if s >= m:
            break    

        if second[s] == first[f]:
            count += 1
            s += 1

    print(count)        
