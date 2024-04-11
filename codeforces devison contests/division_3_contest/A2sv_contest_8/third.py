from bisect import bisect_left,bisect_right

a,m=list(map(int,input().split()))
atck=list(map(int,input().split()))
prefix=[0]
val=[]
keys=[] 

for i in range(m):
    temp=list(map(int,input().split()))
    val.append(temp)
val.sort(key=lambda x :x[0]) 

for i,j in val:
    prefix.append(prefix[-1]+j)
    keys.append(i)
answer=[]

for num in atck:
    ind=bisect_right(keys,num)
    answer.append(prefix[ind])
print(* answer)


