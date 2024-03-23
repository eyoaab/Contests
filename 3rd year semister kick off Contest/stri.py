t = int(input())
s=input()
temp=list(s)
factors=[]
for i in range(1,t+1):
    if t%i==0:
        factors.append(i)
     
for i in factors:
    temp=temp[:i][::-1]+temp[i:]  
print(''.join(temp))     
