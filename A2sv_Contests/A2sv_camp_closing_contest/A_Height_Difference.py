t=int(input())
for _ in range(t):
    li=list(map(int,input().split()))
    height=list(map(int,input().split()))
    n,x=li
    height.sort()
  
    flag=True
    for i in range(n):
        if height[i+n]-x<height[i]:
            print("NO")
            flag=False
            break
    if flag:
        print("YES")    