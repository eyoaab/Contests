from collections import defaultdict
n=int(input())
s1=input()
s2=input()
s=list(s1)
t=list(s2)
ham=0
for i in range(len(s)):
    if t[i]!=s[i]:
        ham+=1
