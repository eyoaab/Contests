def check(num,k):
    return num & (1 << k) == 0
def setbit(num,k):
    num |= (1<<k)
    return num


for _ in range( int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = 0
    for i in range(30,-1,-1):
        count = 0

        for num in nums:
            count += check(num,i) 

        if count <= k:
            k -= count
            answer = setbit(answer,i)

    print(answer)              
