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

 