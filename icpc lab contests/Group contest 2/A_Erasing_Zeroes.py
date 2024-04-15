for _ in range(int(input())):
    name = input()
    nums = []
    for i in range(len(name)):
        if name[i]=='1':
            nums.append(i)

        answer = 0
        for i in range(1,len(nums)):
            answer += nums[i]- nums[i-1]-1
    print(answer)        