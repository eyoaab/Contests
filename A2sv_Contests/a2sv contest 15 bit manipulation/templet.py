def check(num,k):
    return num & (1 << k) != 0
def setbit(num,k):
    num |= (1<<k)
    return num
def offbit(num,k):
    num &= ~(1<<k) 
    return num
def toggle(num,k):
    num ^= (1<<k) 
    return num

 for _ in range(int(input())):
    nums = list(map(int,input().split()))