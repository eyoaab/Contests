stack = "/"  
for _ in range(int(input()) ):
    command = input().split()
    if command[0] == "pwd":
        print(stack)
    else:
        li = command[1]
        if li[0] == '/':
            stack = "/"
            li = li[1:]
        for c in li.split('/'):
            if c == "..":
                stack = '/'.join(stack.split('/')[:-2]) + '/'
            else:
                stack += c + '/'
