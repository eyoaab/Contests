voul = 'AEIOUY'
stack = []
ans = 0
s = input()
for i in range(len(s)):
    if s[i] in voul:
        if not stack:
            ans = i+1
            stack.append(i)
        else:    
            ans = max(ans,i- stack[-1])
            stack.append(i)
if not stack:
    print(len(s)+1)
else: 
    ans = max(ans,len(s) - stack[-1]  )             
    print(ans)        
