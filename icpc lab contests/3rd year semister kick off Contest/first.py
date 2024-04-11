t = int(input())
ref=[]
for i in range(1,2024):
    if 2023%i==0:
        ref.append(i)
    
ref=ref[::-1]
for _ in range(t):
    n,k = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    product=1
    for i in nums:
        product *=i

    if product>2023 or 2023%product!=0 :
        print("NO")
    else: 
        #product=2023-product
        product=2023//product
        ans=[product]
        ans.extend([1]*(k-1))

        print("YES")
        print(*ans)          
