
oprs = input()
stack = []
for ch in oprs:
    if stack and stack[-1] == ch:
        stack.pop()
        continue
    stack.append(ch)  
print('No') if stack else print('Yes')