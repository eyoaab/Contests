from bisect import bisect_left,bisect_right
from collections import defaultdict
import math

string1 = input()
n = int(input())
nums = list(map(int,input().split()))

for _ in range(n):



prefix = [0]
for num in nums:
    prefix.append(num + prefix[-1])