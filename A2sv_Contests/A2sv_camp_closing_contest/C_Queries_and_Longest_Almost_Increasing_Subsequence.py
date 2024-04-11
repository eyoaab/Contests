n,k=list(map(int,input().split()))
nums=list(map(int,input().split()))
def check(left,right):
    _max=0
    count=0
    l=left
    r=left+2
    if right-left<3:
        return right-left+1
    while r<len(nums) and r<=right:
        if nums[r-2]>=nums[r-1]and nums[r-1]>=nums[r]: 
           l+=1
        _max=max(_max,r-l+1)
        r+=1

    return _max    

for _ in range(k):
    temp=list(map(int,input().split()))
    print(check(temp[0]-1,temp[1]-1))

