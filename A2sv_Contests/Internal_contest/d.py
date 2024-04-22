from heapq import *
n = input()
nums = list(map(int,input().split())) 
heap = []
health = 0
answer = 0
for num in nums:
    health += num
    heappush(heap,num)
    if health<0:
        health-=heappop(heap)
    answer = max(answer,len(heap))        
print(answer)    