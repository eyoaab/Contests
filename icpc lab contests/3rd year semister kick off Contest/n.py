s=input()
ans=[]
s=s.lower()
for i in s:
    if i not in 'aeiouy':
        ans.append(i)
print('.'+'.'.join(ans))        