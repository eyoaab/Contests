from math import ceil
from collections import deque
for _ in range(int(input())):
    answer = 0
    n,k = list(map(int,input().split()))
    nums = list(map(int,input().split())) 
    left = ceil(k/2)
    right = k//2  
    for i in range(n):   
        if nums[i]<=left:
            left -= nums[i]       
            nums[i] = 0
        else:
            nums[i]-=left
            left = 0
        if left == 0:
            break   

    for i in range(n-1,-1,-1):

        if nums[i] <= right:
            right -= nums[i] 
            nums[i] = 0
            if right == 0:
                break
            
        else:
            break

    print(nums.count(0))    
