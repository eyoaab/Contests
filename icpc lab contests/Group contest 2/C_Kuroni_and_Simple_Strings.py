s = input()
stack = []
answer = []
for i in range(len(s)):
    if s[i] == '(':
        for j in range(len(s)-1,i,-1):
            if s[j]==')' and (not j in answer):
                answer.append(i)
                answer.append(j)
                break


if answer:
    print(1)
    print(len(answer))
    answer = [i+1 for i in answer]
    print(*sorted(answer)) 
else:
    print(0)                    


