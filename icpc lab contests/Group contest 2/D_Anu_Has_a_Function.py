x=int(input())
nums = list(map(int,input().split()))
ans =[]
odd =[]
even =[]
for i in range(len(nums)):
    if nums[i]%2==0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
odd.sort()           
even.sort()

while odd and even:
    if odd[-1]> even[-1]:
        ans.append(odd.pop())
       
    else:
        ans.append(even.pop())
       
ans.extend(even)
ans.extend(odd) 
print(*ans)        

