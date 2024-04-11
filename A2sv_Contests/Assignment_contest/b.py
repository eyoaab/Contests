for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    _sum = sum(nums)
    nums = [i%3 for i in nums]
    k = _sum%3
    need = (3-k)%3
    if k==0:
        print(0)
    elif (_sum+1)%3 == 0:
        print(1)    
    elif k in nums:
        print(1)
    else:
        print(2)        