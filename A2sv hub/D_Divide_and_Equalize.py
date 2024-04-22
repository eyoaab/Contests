from collections import defaultdict
def count_div(num,coun):
    i = 2
    while i*i <= num:
        while num % i == 0:
            coun[i] += 1
            num //= i
        i += 1
    if num >1:
        coun[num] += 1
    return coun    

for _ in range(int(input())):
    div = defaultdict(int)
    n = int(input())
    nums = list(map(int,input().split())) 
    for num in nums:
        div = count_div(num,div)

    flag = True
    for i,j in div.items():
        if j%n !=0:
            print("NO")
            flag = False
            break        
    if flag:
        print('YES')