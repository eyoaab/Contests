from collections import Counter
n=int(input())
nums= [int(x) for x in input().split()]

stack=[]
c=Counter()
for i in range(len(nums)):
    while stack and nums[stack[-1]] > nums[i]:
        stack.pop()
    if stack:
        if nums[stack[-1]] == nums[i]:
            c[nums[i]] = i - stack[-1] + 1
            stack.pop()
        else:
            c[nums[i]] = i - stack[-1]
    else:
        c[nums[i]] = 1
    stack.append(i)
for i in stack:
    c[nums[i]] += stack[-1] - i
    
print(c)
print(stack)
# d=dict(c)
# d.sort(key=lambda x:(-x[0],x[1]))
# print(d)


