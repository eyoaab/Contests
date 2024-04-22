import heapq
n,k,q = list(map(int,input().split()))
nums = list(map(int,input().split()))
heap = []
for _ in range(q):
    id,val = list(map(int,input().split()))
    if id == 1:
        if len(heap) == k:
            if nums[val-1] <= heap[0]:
                continue
            else: 
                heapq.heappop(heap)
                # heapq.heappushpop(heap,nums[val-1])
                heapq.heappush(heap,nums[val-1])

        else:
            heapq.heappush(heap,nums[val-1])
    else:
        value = nums[val-1]
        if value in heapq.nlargest(k,heap):
            print("YES")
        else:
            print("NO")    