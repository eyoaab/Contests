for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    total = 0
    for num in nums:
        total ^= num

    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp ^= nums[j]

        if temp == nums[i]:
            print(temp)
            break        
        


    