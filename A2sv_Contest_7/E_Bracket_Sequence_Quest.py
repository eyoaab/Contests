from collections import defaultdict
s=input()
stack=[-1]
ref=defaultdict(int)

for i in range(len(s)):
    if s[i]==')':
     
        stack.pop()
        if stack:
            cur=i-stack[-1]
            ref[cur]+=1
        else:
            stack.append(i)    
           
    else:
        stack.append(i)


if ref:
    var=max(ref.keys())   
    for i,j in ref.items():
        if i==var:
            f=i
            s=j
            break
    print(f,s)         
else:
    print(0,1)



