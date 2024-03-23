import math

t = int(input())
for _ in range(t):
    n,hour =  list(map(int,input().split()))
    need = list(map(int,input().split()))
    time = list(map(int,input().split()))

    if sum(time) > hour:
        print(-1) 
    else:
        left = 1
        right = max(need) 
        best = 1
        while left <= right:
            mid = left + (right- left)//2

            _sum = 0
            for i in range(len(need)):
                _sum += math.ceil((need[i]/mid)) * time[i]

            if  _sum <= hour:
                best = mid 
                right = mid -1
            else:
                left = mid +1

        print(best)           
            
