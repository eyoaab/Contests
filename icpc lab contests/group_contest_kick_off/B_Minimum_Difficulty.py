import sys
import random
# input = lambda : sys.stdin.readline
def lis_ch():
    return [i for i in input().split()]
def lis_int():
    return [int(i) for i in input().split()]
n = int(input())
nums = lis_int()
max_ = float('inf')
for i in range(1,n-1):
    subs = nums[::]
    subs.pop(i)
    diff = float('-inf')
    # print(subs)
    for j in range(1,len(subs)):
            diff = max(diff,subs[j] - subs[j-1])
    max_  = min(max_,diff)
print(max_)