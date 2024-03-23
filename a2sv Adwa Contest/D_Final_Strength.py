t = int(input())
def merge(left,right):
   
    n,m=len(left),len(right)
    for i in range(n):
        for j in range(m):
            if left[i] > right[j]:
                nums[i]+=1
            elif left[i] < right[j]: 
                nums[j]+=1   
      
    return left+right           

def devide(left,right):
    if left == right:
        return [nums[left]]
    mid = (left+right)//2

    left_halph =  devide(left,mid)
    right_halph =  devide(mid+1,right) 
    return merge(left_halph,right_halph)

for _ in range(t):
    n = int(input())
    nums =  list(map(int,input().split()))
    devide(0,len(nums)-1)
    print(*nums)

