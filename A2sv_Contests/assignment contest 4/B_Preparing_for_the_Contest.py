from collections import *
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    answer = deque()
    for i in range(k+1):
        answer.appendleft(n)
        n-=1
    for i in range(n,0,-1):
        answer.append(i)  
    print(* answer)      
