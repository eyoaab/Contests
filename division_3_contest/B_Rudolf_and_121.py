t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    if len(set(nums))==1:
        print("No")
    else:
            