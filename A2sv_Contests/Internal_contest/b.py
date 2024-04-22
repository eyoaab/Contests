from heapq import *
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    num1 = list(map(int,input().split()))
    min_heap = []
    for n in num1:
        heappush(min_heap,n)
    num2 = list(map(int,input().split()))    
    for num in num2:
        heapreplace(min_heap,num)
    
    print(sum(min_heap))    