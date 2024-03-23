t = int(input())
s=input()
temp=list(s)
factors=[1]
while t>1:
    factors.append(t)//2
    t=t//2
for i in factors:
    temp=temp[:i][::-1]+temp[i:]  
print(''.join(temp))     
