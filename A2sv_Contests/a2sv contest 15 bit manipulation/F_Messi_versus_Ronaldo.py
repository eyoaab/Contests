def check(num,k):
    return num & (1 << k) != 0

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))

    store = [0 for i in range(64)]

    for num in nums:
        for i in range(64):
            if check(num,i):
                store[i] += 1
    # print(store)            
    mod = 10**9 + 7
    ans = 0 
    
    for num in nums:
        or_ =0
        and_ = 0
        for i in range(60):
            if check(num,i):
                and_ += (store[i] * ( 1<<i ))
                or_ += ( 1<<i  ) * n
            else: 
                or_ += (store[i] * ( 1<<i  ) )

        ans += or_ * and_

    print(ans % mod)                        