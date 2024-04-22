for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    s = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    c= 0
    for i in range(a):
        answer += s[c]
        c+=1
        if c== b:
            c=0
    print(answer)