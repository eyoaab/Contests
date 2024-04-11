    # ok
from functools import cmp_to_key
arr = [2,7, -7,2,3,-3,-2,3, -2, -2, 0]

def comp(a,b):
    if abs(a) > abs(b): return 1
    if abs(a) < abs(b): return -1
    if a > b: return 1
    if b > a: return -1
    return 0
print(sorted(arr,key= cmp_to_key(comp)))