import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def fireworks(a, b, m):
    lcm_ab = lcm(a, b)
    fireworks_a = lcm_ab // a
    fireworks_b = lcm_ab // b
    total_fireworks = fireworks_a + fireworks_b
    return (m // lcm_ab) * total_fireworks + min((m % lcm_ab) + 1, total_fireworks)


t = int(input())
for _ in range(t):
    a, b, m = map(int,input().split())
    print(fireworks(a, b, m))
