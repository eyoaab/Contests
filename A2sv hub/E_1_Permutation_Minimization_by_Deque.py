from collections import deque
for _ in range(int(input())):
    result = deque()
    n = int(input())
    nums  = list(map(int,input().split()))

    for num in nums:
        if result:
            if result[0]>num:
                result.appendleft(num)
            else:
                result.append(num)
        else:
            result.append(num)

    print(* result)                
