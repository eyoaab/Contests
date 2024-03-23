t =int(input())

for _ in range(t):
    n,l =  list(map(int,input().split()))
    flag = False
    ss1 =input()
    ss2 = input()

    prefix = [0]
    _sum=0
    for i in ss2:
        _sum += ord(i)
    for num in ss1:
        prefix.append(ord(num) + prefix[-1]) 
    #prefix = prefix[1:]
    #print(_sum)     

    if len(ss1)<len(ss2): 
        flag=False
    else:
        r=len(ss2)
        while r < len(prefix):
            if  prefix[r]-prefix[r-len(ss2)]==_sum:
                #print(ss1[r-len(ss2):r])
                flag = True
                break 
            r+=1    
      
    if flag :
        print("YES")
    else:
        print("NO")    