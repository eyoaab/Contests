for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]

    ans = 3
    for i in range(n):
        if i + 1 == nums[nums[i] - 1]:
            ans = 2
            break
    
    print(ans)
    