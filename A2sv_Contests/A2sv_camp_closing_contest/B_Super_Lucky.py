n=int(input())
""""def check(s):
    if len(s)%2!=0:
        return False
    return s.count('7')== s.count('4')==len(s)//2
"""

s=str(n)
if n<47:
    n=47
elif len(s)%2!=0:
    l=len(s)
    n=pow(10,l)*4
s=str(n)
 
ans=[]
def victim(v):
    return int(v[0])>7   


if victim(s):
    s='44'+s
num=list(s)    
four=seven=len(num)//2
for i in range(len(num)):
    if four>0 and int(num[i])<=4:
        num[i]='4'
        four-=1
    else:
        num[i]='7'
       
    

n=int(''.join(num))
print(n)           