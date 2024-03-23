from bisect import bisect_left,bisect_right
#lli=list(map(int,input().split()))
t=int(input())
for _ in range(t):
    size,dig=list(map(int,input().split()))
    num=input()
    flag=True
    ans=len(num)
    for i in range(len(num)):
        if int(num[i])<dig and flag:
            flag=False
            ans=i
    num=list(num)
    num.insert(ans,str(dig))        
        
    print(''.join(num))
  
   
    
    
    