import math

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
   
    new_arr = [max(ar)+ 1]
    
    for num in ar:
        new_arr.append(new_arr[-1] + num) 

    print(*new_arr)
