from heapq import *
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    answer = 0
    heap = []
    for num in nums:
        if num == 0:
            if heap:
                answer += -heappop(heap)
        else:
            heappush(heap,-num) 
    print(answer)               
