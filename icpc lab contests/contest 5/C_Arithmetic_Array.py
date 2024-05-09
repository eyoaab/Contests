import sys
input = lambda : sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(i) for i in  input().split()]
    # print(nums)
    sm = sum(nums)
    if sm/n == 1:
        print(0)
        continue
    if sm > 0 and sm > n:
        print(sm - n)
    else:
        print(1)