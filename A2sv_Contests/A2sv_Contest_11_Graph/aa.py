from collections import defaultdict
n,m = list(map(int,input().split()))
Flag = True
count = []
for i in range(n):
    row = input()
    if len(set(row))>1:
        Flag = False
        break
    if count and count[-1] == row[0]:
        Flag = False
    count.append(row[0])    
     
if Flag: 
    print("YES")
else:
    print("NO")                