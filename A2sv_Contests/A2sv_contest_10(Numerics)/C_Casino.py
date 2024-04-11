def check(n):
    # while n!=1:
    #     if n%2==0:
    #         n=n//2
    #     elif n%3 ==0:
    #         n=n//3
    #     else:
    #         return n 
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    
    return n               
ans = set()

t= int(input())    
nums = list(map(int,input().split()))
for num in nums:
    ans.add(check(num))

if len(ans)==1:
    print("Yes")
else:
    print("No")            