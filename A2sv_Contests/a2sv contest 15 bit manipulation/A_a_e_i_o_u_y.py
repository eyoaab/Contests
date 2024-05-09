n = int(input())
s = input()
v = 'aeiouy'
an = s[0]
for i in range(1,n):
    if not(s[i] in v and an[-1]  in v):
            an += s[i]    
print(an)            