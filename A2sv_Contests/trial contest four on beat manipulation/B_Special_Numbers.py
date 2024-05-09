MOD = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    answer = 0
    power = 0
    while k > 0:
        bit = k & 1
        if bit == 1:
            answer = (answer + pow(n, power, MOD)) % MOD
        power += 1
        k >>= 1
    print(answer)
