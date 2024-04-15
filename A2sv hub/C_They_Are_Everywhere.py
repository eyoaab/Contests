from collections import defaultdict
n  = int(input())
s =  input()
target = len(set(s))
answer = n
referance = defaultdict(int)
left =  0

for right in range(n):
    referance[s[right]] += 1
    if len(referance) == target:
        
        while len(referance) == target:
            answer = min(answer,right - left + 1)
            referance[s[left]] -= 1
            if referance[s[left]] == 0:
                del referance[s[left]]
            left +=1


print(answer)            
