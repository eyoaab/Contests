from collections import Counter
t=int(input())
for _m in range(t):
    n=int(input())
    first=input()
    temp=Counter(first)
    for i in range(n-1):
        second=input()
        temp+=Counter(second)
        
    flag=False    
    for i in temp:
        if temp[i]%n!=0:
               flag=True 
               break
    if flag:
         print("NO")
    else: 
         print("YES")    