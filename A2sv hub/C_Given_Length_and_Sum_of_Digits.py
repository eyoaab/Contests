m,s = map(int,input().split()) 
nums = []
if s == 0 and m == 1:
  print(0,0)
  exit()
elif s == 0 or (9 * m) < s:
  print(-1 ,-1)
  exit()

else:
  while m > 0:
    curr  = min(s,9)
    nums.append(curr)
    s -= curr
    m -= 1

reversed_arr = nums[::-1]
j = 0~
while reversed_arr[j] == 0:
  j += 1

reversed_arr[0] += 1
reversed_arr[j] -= 1


minn=""
maxx=""
for i in nums:
  maxx+=str(i)
for j in reversed_arr:
  minn+=str(j)

print(minn,maxx)

