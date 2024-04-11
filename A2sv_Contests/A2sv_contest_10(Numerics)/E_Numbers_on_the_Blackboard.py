import math
def helper():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if nums.count(nums[0]) == n:
        return 0
    for num in nums:
        if (num >= k and nums[0] <= k) or (num <= k and nums[0] >= k):
            return -1
    gcd = abs(k - nums[0])
    for num in nums:
   	    gcd = math.gcd(gcd, abs(k - num)) 
    res = 0
    for num in nums:
        res += (abs(k - num) // gcd - 1)
    
    return res

for _ in range(int(input())):
   	    print(helper())