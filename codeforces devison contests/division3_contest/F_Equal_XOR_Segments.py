for _ in range(int(input())):
    n,m =  list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    for i in range(m):
        l,r =  list(map(int, input().split()))
        num = 0
        for k in nums[l-1:r]:
            num ^= k

        if  num:
            print(num)
            print('YES')
        else:
            print("NO")        