for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    nums = [abs(i) for i in nums]
    print(sum(nums))